import click

from .subshell import SubShell
from .database import DatabaseShell

from readop.managers.parameters import ParameterManager
from readop.models.parameters import Parameters


class ParameterShell(SubShell):
    intro = \
        SubShell.separator + \
        'ReadOp Parameter subsystem.\n' + \
        SubShell.instruction_for_help + \
        SubShell.separator

    prompt = 'readop parameters > '

    def __init__(self):
        super().__init__()
        self.parameter_manager = ParameterManager()
        self.database_shell = DatabaseShell()

    def do_get(self, user_input):
        storage_unit = self.database_shell.choose_storage_unit()
        parameters = self.parameter_manager.get_parameters(storage_unit.name)
        print(parameters)

    def help_get(self):
        print('Gets parameters from a storage unit.')

    def do_set(self, user_input):
        storage_unit = self.database_shell.choose_storage_unit()
        parameters = self.prompt_for_parameters()
        self.parameter_manager.set_parameters(storage_unit.name, parameters)

    def help_set(self):
        print('Sets parameters on a storage unit.')

    def prompt_for_parameters(self) -> Parameters:
        return Parameters(
            default_access_pattern=click.prompt(
                'default_access_pattern',
                type=int,
                default=Parameters.DEFAULT_ACCESS_PATTERN
            ),
            apd_data_seq_threshold=click.prompt(
                'apd_data_seq_threshold',
                type=int,
                default=Parameters.APD_DATA_SEQ_THRESHOLD
            ),
            init_io_region_size=click.prompt(
                'init_io_region_size',
                type=int,
                default=Parameters.INIT_IO_REGION_SIZE
            ),
            max_io_regions=click.prompt(
                'max_io_regions',
                type=int,
                default=Parameters.MAX_IO_REGIONS
            ),
            apd_access_seq_threshold=click.prompt(
                'apd_access_seq_threshold',
                type=int,
                default=Parameters.APD_ACCESS_SEQ_THRESHOLD
            ),
            apd_access_random_threshold=click.prompt(
                'apd_access_random_threshold',
                type=int,
                default=Parameters.APD_ACCESS_RANDOM_THRESHOLD
            ),
            apd_access_random_inc_threshold=click.prompt(
                'apd_access_random_inc_threshold',
                type=int,
                default=Parameters.APD_ACCESS_RANDOM_INC_THRESHOLD
            )
        )
