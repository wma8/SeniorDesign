"""
Contains functionality for executing operations.
"""

from readop.managers.database import DatabaseManager
from readop.managers.ddboost import DDBoostManager
from readop.managers.ddve import DDVEManager
from readop.managers.parameters import ParameterManager
from readop.database.models.operation import Operation


class OperationManager:
    """
    Maintains the subsystems required for the execution of an operation.
    """

    def __init__(self):
        """
        Initializes the subsystems required for the execution of an operation.
        """

        self.ddve = DDVEManager()
        self.ddboost = DDBoostManager()
        self.parameters = ParameterManager()
        self.database = DatabaseManager()

    def execute_operation(self, operation: Operation) -> None:
        """
        Executes an operation by passing it to the subsystems in the proper order.

        :param operation: operation inputs and storage for outputs
        :return: None, modifies the operation object by reference.
        """

        storage_unit = self.database.get_storage_unit_by_id(operation.storage_unit_id)

        self.ddve.clear_results()
        self.parameters.set_parameters(
            storage_unit.name,
            operation.parameters
        )
        self.ddboost.execute(operation)
        self.ddve.get_results(operation)
        self.database.save(operation)
