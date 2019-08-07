from readop.database.session import Session
from readop.database.models import AccessPattern, Operation, StorageUnit, SystemDescription, WorkloadDescription

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


class DatabaseManager:
    def __init__(self):
        self._session = Session()

    def __del__(self):
        self._session.commit()
        self._session.close()

    def save(self, database_model):
        self._session.add(database_model)
        self._session.commit()

    def get_all(self, cls):
        return self._session.query(cls).all()

    def get_access_pattern_by_id(self, ap_id: int) -> AccessPattern:
        try:
            return self._session.query(AccessPattern).filter(AccessPattern.id == ap_id).one()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)

    def get_operation_by_id(self, op_id: int) -> Operation:
        try:
            return self._session.query(Operation).filter(Operation.id == op_id).one()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)

    def get_storage_unit_by_id(self, su_id: int) -> StorageUnit:
        try:
            return self._session.query(StorageUnit).filter(StorageUnit.id == su_id).one()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)

    def get_system_description_by_id(self, sd_id: int) -> SystemDescription:
        try:
            return self._session.query(SystemDescription).filter(SystemDescription.id == sd_id).one()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)

    def get_workload_description_by_id(self, wd_id: int) -> WorkloadDescription:
        try:
            return self._session.query(WorkloadDescription).filter(WorkloadDescription.id == wd_id).one()
        except MultipleResultsFound as e:
            print(e)
        except NoResultFound as e:
            print(e)
