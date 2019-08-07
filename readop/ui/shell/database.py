import click

from .subshell import SubShell

from readop.database.models import AccessPattern, StorageUnit, SystemDescription, WorkloadDescription
from readop.managers.database import DatabaseManager


class DatabaseShell(SubShell):
    ACCESS_PATTERN = 'Access Pattern'
    STORAGE_UNIT = 'Storage Unit'
    SYSTEM_DESCRIPTION = 'System Description'
    WORKLOAD_DESCRIPTION = 'Workload Description'

    DATABASE_RECORD_TYPES = [
        ACCESS_PATTERN,
        STORAGE_UNIT,
        SYSTEM_DESCRIPTION,
        WORKLOAD_DESCRIPTION
    ]

    intro = \
        SubShell.separator +\
        'ReadOp Database subsystem.\n' + \
        SubShell.instruction_for_help + \
        SubShell.separator

    prompt = 'readop database > '

    def __init__(self):
        super().__init__()
        self.database_manager = DatabaseManager()

    def do_create(self, user_input):
        record_type_choice = self.choose_database_record_type()

        if record_type_choice == self.ACCESS_PATTERN:
            self.prompt_create_access_pattern()
        elif record_type_choice == self.STORAGE_UNIT:
            self.prompt_create_storage_unit()
        elif record_type_choice == self.SYSTEM_DESCRIPTION:
            self.prompt_create_system_description()
        elif record_type_choice == self.WORKLOAD_DESCRIPTION:
            self.prompt_create_workload_description()

        print()

    def help_create(self):
        print('Enables saving records into the database.')

    def do_show(self, user_input):
        record_type_choice = self.choose_database_record_type()

        if record_type_choice == self.ACCESS_PATTERN:
            self.print_all_access_patterns()
        elif record_type_choice == self.STORAGE_UNIT:
            self.print_all_storage_units()
        elif record_type_choice == self.SYSTEM_DESCRIPTION:
            self.print_all_system_descriptions()
        elif record_type_choice == self.WORKLOAD_DESCRIPTION:
            self.print_all_workload_descriptions()

        print()

    def help_show(self):
        print('Shows records currently in the database.')

    def _get_all(self, cls):
        return self.database_manager.get_all(cls)

    def _print_all(self, cls):
        for record in self._get_all(cls):
            print(record)

    def print_all_access_patterns(self):
        self._print_all(AccessPattern)

    def print_all_storage_units(self):
        self._print_all(StorageUnit)

    def print_all_system_descriptions(self):
        self._print_all(SystemDescription)

    def print_all_workload_descriptions(self):
        self._print_all(WorkloadDescription)

    def choose_access_pattern(self):
        print('Available Access Pattern records:')
        self.print_all_access_patterns()

        access_pattern_id = click.prompt('Enter an Access Pattern id', type=int)

        return self.database_manager.get_access_pattern_by_id(access_pattern_id)

    def choose_database_record_type(self) -> str:
        print('Database record types available:')
        for i in range(len(self.DATABASE_RECORD_TYPES)):
            print('[{0}] {1}'.format(i, self.DATABASE_RECORD_TYPES[i]))

        choice = click.prompt(
            'Choose from the options above',
            type=click.IntRange(0, len(self.DATABASE_RECORD_TYPES) - 1)
        )

        print()

        return self.DATABASE_RECORD_TYPES[int(choice)]

    def choose_storage_unit(self):
        print('Available Storage Unit records:')
        self.print_all_storage_units()

        storage_unit_id = click.prompt('Enter a Storage Unit id', type=int)

        return self.database_manager.get_storage_unit_by_id(storage_unit_id)

    def prompt_create_access_pattern(self):
        print('Access Pattern records require a foreign key to a Workload Description record.')
        print('Available Workload Description records:')
        self.print_all_workload_descriptions()

        workload_description_id = click.prompt('Enter a Workload Description id', type=int)
        file_path = click.prompt('AccessPattern.file_path')

        access_pattern = AccessPattern(file_path, workload_description_id)
        self.database_manager.save(access_pattern)

        print('Access Pattern record saved successfully.')

    def prompt_create_storage_unit(self) -> None:
        name = click.prompt('storage_unit.name')

        storage_unit = StorageUnit(name)
        self.database_manager.save(storage_unit)

        print('Storage Unit record saved successfully:')
        print(storage_unit)

    def prompt_create_system_description(self) -> None:
        description = click.prompt('system_description.description')

        system_description = SystemDescription(description)
        self.database_manager.save(system_description)

        print('System Description record saved successfully:')
        print(system_description)

    def prompt_create_workload_description(self) -> int:
        description = click.prompt('workload_description.description')

        workload_description = WorkloadDescription(description)
        self.database_manager.save(workload_description)

        print('Workload Description record created successfully:')
        print(workload_description)

        return workload_description.id
