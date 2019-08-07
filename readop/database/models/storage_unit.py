from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base, string_length


class StorageUnit(Base):
    __tablename__ = 'storage_units'

    _id = Column('id', Integer, primary_key=True)
    _name = Column('name', String(string_length), nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return '<StorageUnit id={0}, name=\'{1}\'>'.format(self.id, self.name)

    @hybrid_property
    def id(self) -> int:
        return self._id

    @hybrid_property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError

        self._name = name
