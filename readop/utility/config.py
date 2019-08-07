import os
import yaml


def read_configuration_file(file_path: str = 'readop/config.yaml') -> None:
    if os.path.isfile(file_path):
        with open(file_path, 'r') as stream:
            try:
                global configuration_data
                configuration_data = yaml.safe_load(stream)
            except yaml.YAMLError as e:
                print(e)


def get_config(*config_path) -> str:
    global configuration_data, configuration_was_loaded

    if not configuration_was_loaded:
        read_configuration_file()
        configuration_was_loaded = True

    config = configuration_data
    for item in config_path:
        config = config[item]

    return config


def get_ddve_host() -> str:
    return get_config('ddve', 'host')


def get_ddve_username() -> str:
    return get_config('ddve', 'username')


def get_ddve_password() -> str:
    return get_config('ddve', 'password')


def get_ddve_rest_port() -> str:
    return get_config('ddve', 'rest_port')


def get_database_host() -> str:
    return get_config('database', 'host')


def get_database_port() -> str:
    return get_config('database', 'port')


def get_database_username() -> str:
    return get_config('database', 'username')


def get_database_password() -> str:
    return get_config('database', 'password')


def get_database_name() -> str:
    return get_config('database', 'name')


def get_debug_database_engine_echo() -> str:
    return get_config('debug', 'database_engine_echo')


configuration_was_loaded = False
configuration_data = {
    'ddve': {
        'host': '192.168.41.52',
        'username': 'sysadmin',
        'password': 'sdcTeam21',
        'rest_port': '3009'
    },
    'database': {
        'host': 'localhost',
        'port': '3306',
        'username': 'root',
        'password': 'sdcTeam21!',
        'name': 'ReadOp'
    },
    'debug': {
        'database_engine_echo': False
    }
}
