from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.helpers.errors.domain_errors import EntityError


class CreateCriminalRecordUsecase:
    def __init__(self, repo_criminal_record : ICriminalRecordRepository):
        self.repo_criminal_record = repo_criminal_record

    def __call__(self,criminal_record: CriminalRecord) -> CriminalRecord:

        if not CriminalRecord.validade_danger_score(criminal_record.danger_score):
            raise EntityError("danger_score")
        
        return self.repo_criminal_record.create_criminal_record(criminal_record=criminal_record)
