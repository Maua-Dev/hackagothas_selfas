from abc import ABC
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class Crime(ABC):
    id: str
    type_crime: TYPE_CRIME

    def __init__(self, id: str, type_crime: TYPE_CRIME):
        if type(id) != str:
            raise EntityError("id")
        self.id = id

        if type(type_crime) != TYPE_CRIME:
            raise EntityError("type_crime")
        self.type_crime = TYPE_CRIME
