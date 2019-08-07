import csv
import traceback

from readop.managers.operation import OperationManager
from readop.database.models.operation import Operation
from readop.utility import validator


class AutomationManager:
    def __init__(self, operation_list_path: str) -> None:
        validator.validate_string_not_empty(operation_list_path)

        self.operation_manager = OperationManager()
        self.out_file = open(operation_list_path + '-output', 'w+')

        self.log('Parsing operation list...')

        with open(operation_list_path) as csv_file:
            reader = csv.reader(csv_file, skipinitialspace=True)
            self.operation_list = list(reader)

        self.operation_count = len(self.operation_list)

        self.log(' success ({0} items read).\n'.format(str(self.operation_count)))

    def execute_operations(self):

        self.log('Executing {0} operations:\n'.format(str(self.operation_count)))
        self.log('------------------------------------------------------------\n')
        self.log('{0:<15} | {1:<15} | {2:<15}\n'.format('Operation #', 'Time (ms)', 'Status'))
        self.log('------------------------------------------------------------\n')

        success_count = 0
        failure_count = 0

        for i in range(self.operation_count):
            op = Operation.from_array(self.operation_list[i])

            self.log('{0:<15} | '.format(i))
            self.out_file.flush()

            output = ''

            try:
                self.operation_manager.execute_operation(op)
                output += '{0:<15} | {1:<15}'.format(str(op.execution_time), 'Success')
                success_count += 1
            except Exception as e:
                output += '{0:<15} | {1:<15}'.format('0', 'Failure') + '\n\n'
                output += 'Error: {0}'.format(str(e)) + '\n\n'
                output += traceback.format_exc()
                failure_count += 1

            self.log(output + '\n')

        self.log('------------------------------------------------------------\n')
        self.log('Finished executing {0} operations.\n'.format(str(self.operation_count)))
        self.log('{0:<12}: {1}\n'.format('Successes', str(success_count)))
        self.log('{0:<12}: {1}\n'.format('Failures', str(failure_count)))

    def log(self, message: str) -> None:
        print(message, end='')
        self.out_file.write(message)
        self.out_file.flush()
