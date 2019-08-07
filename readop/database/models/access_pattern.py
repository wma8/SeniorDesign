from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from .base import Base, string_length
from .workload_description import WorkloadDescription


class AccessPattern(Base):
    __tablename__ = 'access_patterns'

    _id = Column('id', Integer, primary_key=True)
    _file_path = Column('file_path', String(string_length), nullable=False)
    _workload_description_id = Column(
        'workload_description_id',
        Integer,
        ForeignKey('workload_descriptions.id'),
        nullable=False
    )

    _workload_description = relationship('WorkloadDescription')

    def __init__(self, file_path: str, workload_description_id: int) -> None:
        self.file_path = file_path
        self.workload_description_id = workload_description_id

    def __repr__(self) -> str:
        return '<AccessPattern id={0}, file_path=\'{1}\', workload_description_id={2}>'.format(
            self.id,
            self.file_path,
            self.workload_description_id
        )

    @hybrid_property
    def id(self) -> int:
        return self._id

    @hybrid_property
    def name(self) -> str:
        return self._file_path

    @hybrid_property
    def file_path(self) -> str:
        return self._file_path

    @hybrid_property
    def workload_description_id(self) -> int:
        return self._workload_description_id

    @hybrid_property
    def workload_description(self) -> WorkloadDescription:
        return self._workload_description

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        if not isinstance(file_path, str):
            raise TypeError
        if not file_path:
            raise ValueError

        self._file_path = file_path

    @workload_description_id.setter
    def workload_description_id(self, workload_description_id: int) -> None:
        if not isinstance(workload_description_id, int):
            raise TypeError
        if not workload_description_id:
            raise ValueError

        self._workload_description_id = workload_description_id
