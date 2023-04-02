from abc import ABC
from helpers.errors.domain_errors import EntityError
from enums.type_crime_enum import TYPE_CRIME
from entities.criminal_entity import Criminal


class Crime(ABC):
    id: str
    type_crime: TYPE_CRIME
    criminal: Criminal

    def __init__(self, id: str, type_crime: TYPE_CRIME, criminal: Criminal):
        if type(id) != str:
            raise EntityError("id")
        self.id = id

        if type(type_crime) != TYPE_CRIME:
            raise EntityError("type_crime")
        self.type_crime = TYPE_CRIME
