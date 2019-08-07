import json
import requests
import urllib3

import readop.utility.config as config
from readop.models.credentials import Credentials
from readop.models.parameters import Parameters
from readop.utility import validator

# suppresses SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _response_data_to_parameters(response_data: dict) -> Parameters:
    parameters = Parameters()

    if 'tagset' not in response_data:
        raise ValueError('Expected tagset field in response data')

    tagset = response_data['tagset']

    for tag in tagset:
        if 'key' not in tag:
            raise ValueError('Expected key in tag')
        if 'value' not in tag:
            raise ValueError('Expected value in tag')

        key = tag['key']
        value = int(tag['value'])

        if key == 'OST_DEFAULT_ACCESS_PATTERN':
            parameters.default_access_pattern = value
        elif key == 'OST_APD_DATA_SEQ_THRESHOLD':
            parameters.apd_data_seq_threshold = value
        elif key == 'OST_INIT_IO_REGION_SIZE':
            parameters.init_io_region_size = value
        elif key == 'OST_MAX_IO_REGIONS':
            parameters.max_io_regions = value
        elif key == 'OST_APD_ACCESS_SEQ_THRESHOLD':
            parameters.apd_access_seq_threshold = value
        elif key == 'OST_APD_ACCESS_RANDOM_THRESHOLD':
            parameters.apd_access_random_threshold = value
        elif key == 'OST_APD_ACCESS_RANDOM_INC_THRESHOLD':
            parameters.apd_access_random_inc_threshold = value
        else:
            raise ValueError('Unexpected tag in response: {0}'.format(key))

    return parameters


def _parameters_to_response_body(parameters):
    return {
        'mdtag_object_modify': {
            'namespace': 'file',
            'tagset': [
                {
                    'key': 'OST_DEFAULT_ACCESS_PATTERN',
                    'value': 'int:' + str(parameters.default_access_pattern)
                },
                {
                    'key': 'OST_APD_DATA_SEQ_THRESHOLD',
                    'value': 'int:' + str(parameters.apd_data_seq_threshold)
                },
                {
                    'key': 'OST_INIT_IO_REGION_SIZE',
                    'value': 'int:' + str(parameters.init_io_region_size)
                },
                {
                    'key': 'OST_MAX_IO_REGIONS',
                    'value': 'int:' + str(parameters.max_io_regions)
                },
                {
                    'key': 'OST_APD_ACCESS_SEQ_THRESHOLD',
                    'value': 'int:' + str(parameters.apd_access_seq_threshold)
                },
                {
                    'key': 'OST_APD_ACCESS_RANDOM_THRESHOLD',
                    'value': 'int:' + str(parameters.apd_access_random_threshold)
                },
                {
                    'key': 'OST_APD_ACCESS_RANDOM_INC_THRESHOLD',
                    'value': 'int:' + str(parameters.apd_access_random_inc_threshold)
                }
            ]
        }
    }


class AuthenticationException(Exception):
    pass


class InvalidAuthTokenException(Exception):
    pass


class HTTP:
    def __init__(self):
        self.auth_token = 'NOT YET AUTHENTICATED'
        self.credentials = Credentials(config.get_ddve_username(), config.get_ddve_password())
        self.url = 'https://' + config.get_ddve_host() + ':' + config.get_ddve_rest_port() + '/rest/v1.0'

        self.authenticate()
    
    def authenticate(self):
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
       
        body = {
            'auth_info': {
                'username': self.credentials.username,
                'password': self.credentials.password
            }
        }
        
        url = self.url + '/auth'
        
        response = requests.post(url, headers=headers, json=body, verify=False)
        
        if not response.headers['X-DD-AUTH-TOKEN']:
            raise AuthenticationException('Failed to authenticate')

        self.auth_token = response.headers['X-DD-AUTH-TOKEN']

    def get_parameters(
            self,
            storage_unit: str,
            should_authenticate: bool = False
    ) -> Parameters:
        if should_authenticate:
            self.authenticate()
        
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/text',
            'X-DD-AUTH-TOKEN': self.auth_token
        }
        
        url = self.url + '/dd-systems/0/mdtags/%2Fdata%2Fcol1%2F' + storage_unit + '?filter=namespace%3Dfile'
        
        response = requests.get(url, headers=headers, verify=False)
        response_data = json.loads(response.text)
        
        if response.status_code == 302 and response_data['code'] == 5427:
            raise InvalidAuthTokenException
                
        return _response_data_to_parameters(response_data)
    
    def set_parameters(
            self,
            storage_unit: str,
            parameters: Parameters,
            should_authenticate: bool = False
    ) -> None:
        if should_authenticate:
            self.authenticate()
        
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/text',
            'X-DD-AUTH-TOKEN': self.auth_token
        }
        
        body = _parameters_to_response_body(parameters)
        
        url = self.url + '/dd-systems/0/mdtags/%2Fdata%2Fcol1%2F' + storage_unit
        
        response = requests.put(url, headers=headers, json=body, verify=False)
        response_data = json.loads(response.text)
        
        if response.status_code == 302 and response_data['code'] == 5427:
            raise InvalidAuthTokenException
    
    @property
    def auth_token(self):
        return self.__auth_token
    
    @property
    def credentials(self):
        return self.__credentials
    
    @property
    def url(self):
        return self.__url
    
    @auth_token.setter
    def auth_token(self, auth_token):
        self.__auth_token = validator.validate_string_not_empty(auth_token)
    
    @credentials.setter
    def credentials(self, credentials):
        self.__credentials = validator.validate_credentials(credentials)
    
    @url.setter
    def url(self, url):
        self.__url = validator.validate_string_not_empty(url)
