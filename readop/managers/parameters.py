"""
Interactions with DDVE Parameter system.
"""

import argparse

from readop.models.parameters import Parameters
from readop.protocols.http import HTTP
from readop.protocols.http import InvalidAuthTokenException


def _create_arg_parser():
    parser = argparse.ArgumentParser(description='DDBoost parameter getter/setter.')

    parser.add_argument('storage_unit', help='name of storage unit to interact with')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--get', '-g', action='store_true', help='get the parameters currently set')
    group.add_argument('--set', '-s', action='store_true', help='parameters to set')

    parser.add_argument('--default', '-d', action='store_true', help='use the default parameter values')

    return parser


def _parse_args(args_list=None):
    parser = _create_arg_parser()

    if args_list is None:
        return parser.parse_args()
    else:
        parser.prog = 'parameters'
        return parser.parse_args(args_list)


def _should_use_default(text: str) -> bool:
    return text == 'd' or text == 'default'


def _prompt_for_parameters() -> Parameters or None:
    parameters = Parameters()

    print('\nEnter values for the following parameters.')
    print('Type \'d\' or \'default\' for default value.\n')

    try:
        # prompt for default_access_pattern
        user_input = input(
            'default_access_pattern (default = {0}): '.format(Parameters.DEFAULT_ACCESS_PATTERN)
        )
        if not _should_use_default(user_input):
            parameters.default_access_pattern = int(user_input)

        # prompt for apd_data_seq_threshold
        user_input = input(
            'apd_data_seq_threshold (default = {0}): '.format(Parameters.APD_DATA_SEQ_THRESHOLD)
        )
        if not _should_use_default(user_input):
            parameters.apd_data_seq_threshold = int(user_input)

        # prompt for init_io_region_size
        user_input = input(
            'init_io_region_size (default = {0}): '.format(Parameters.INIT_IO_REGION_SIZE)
        )
        if not _should_use_default(user_input):
            parameters.init_io_region_size = int(user_input)

        # prompt for max_io_regions
        user_input = input(
            'max_io_regions (default = {0}): '.format(Parameters.MAX_IO_REGIONS)
        )
        if not _should_use_default(user_input):
            parameters.max_io_regions = int(user_input)

        # prompt for apd_access_seq_threshold
        user_input = input(
            'apd_access_seq_threshold (default = {0}): '.format(Parameters.APD_ACCESS_SEQ_THRESHOLD)
        )
        if not _should_use_default(user_input):
            parameters.apd_access_seq_threshold = int(user_input)

        # prompt for apd_access_random_threshold
        user_input = input(
            'apd_access_random_threshold (default = {0}): '.format(Parameters.APD_ACCESS_RANDOM_THRESHOLD)
        )
        if not _should_use_default(user_input):
            parameters.apd_access_random_threshold = int(user_input)

        # prompt for apd_access_random_inc_threshold
        user_input = input(
            'apd_access_random_inc_threshold (default = {0}): '.format(Parameters.APD_ACCESS_RANDOM_INC_THRESHOLD)
        )
        if not _should_use_default(user_input):
            parameters.apd_access_random_inc_threshold = int(user_input)

    except ValueError:
        return None

    return parameters


def _get_parameters(use_default: bool) -> Parameters:
    if use_default:
        return Parameters()
    else:
        parameters = None
        while parameters is None:
            print('Invalid value, please enter an integer.')
            parameters = _prompt_for_parameters()
        return parameters


class ParameterManager:
    """
    Handles credential management and re-authentication for rest http communication.
    """
    
    def __init__(self):
        """
        Initialize the HTTP protocol instance.
        """

        self.http = HTTP()
    
    def get_parameters(self, storage_unit_name: str) -> Parameters:
        """
        Returns the parameters currently set on the storage unit.

        :param storage_unit_name: storage unit to retrieve parameters from
        :return: parameters currently set on the storage unit
        """

        try:
            return self.http.get_parameters(storage_unit_name)
        except InvalidAuthTokenException:
            return self.http.get_parameters(storage_unit_name, True)

    def set_parameters(self, storage_unit_name: str, parameters: Parameters) -> None:
        """
        Sets the parameters on the specified storage unit.

        :param storage_unit_name: storage unit to set parameters on.
        :param parameters: parameter values to be set.
        :return:
        """

        try:
            self.http.set_parameters(storage_unit_name, parameters)
        except InvalidAuthTokenException:
            self.http.set_parameters(storage_unit_name, parameters, True)
