from abc import ABC
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.entities.criminal_entity import Criminal


class CriminalRecord(ABC):
    id: str
    type_crime: TYPE_CRIME
    is_in_jail: bool
    danger_score: int
    criminal: Criminal

    def __init__(self, id: str, type_crime: TYPE_CRIME, is_in_jail: bool, danger_score: int, criminal: Criminal):
        if type(id) != str:
            raise EntityError("id")
        self.id = id

        if type(type_crime) != TYPE_CRIME:
            raise EntityError("type_crime")
        self.type_crime = type_crime

        if type(is_in_jail) != bool:
            raise EntityError("is_in_jail")
        self.is_in_jail = is_in_jail

        if type(danger_score) != int:
            raise EntityError("danger_score")
        self.danger_score = danger_score

        if type(criminal) != Criminal:
            raise EntityError("criminal")
        self.criminal = criminal

    @staticmethod
    def validade_danger_score(score:int) -> bool:
        if(type(score) != int):
            return False
        if(score < 0):
            return False
        if(score > 100):
            return False
        return True
