from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property

from .base import Base, string_length


class SystemDescription(Base):
    __tablename__ = 'system_descriptions'

    _id = Column('id', Integer, primary_key=True)
    _description = Column('description', String(string_length), nullable=False)

    def __init__(self, description: str) -> None:
        self.description = description

    def __repr__(self) -> str:
        return '<SystemDescription id={0}, description=\'{1}\'>'.format(self.id, self.description)

    @hybrid_property
    def id(self) -> int:
        return self._id

    @hybrid_property
    def name(self) -> str:
        return self._description

    @hybrid_property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        if not isinstance(description, str):
            raise TypeError
        if not description:
            raise ValueError

        self._description = description
