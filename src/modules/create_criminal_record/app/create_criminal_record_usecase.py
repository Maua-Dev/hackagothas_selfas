from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.helpers.errors.domain_errors import EntityError


class CreateCriminalRecordUseCase:
    def __init__(self, repo : ICriminalRecordRepository):
        self.repo = repo

    def __call__(self, id: str, type_crime: TYPE_CRIME, is_in_jail: bool, danger_score:int, criminal: Criminal) -> CriminalRecord:
            
        if not CriminalRecord.validade_danger_score(danger_score):
            raise EntityError("danger_score")
