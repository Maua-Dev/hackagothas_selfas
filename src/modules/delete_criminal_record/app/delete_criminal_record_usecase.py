from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository


class DeleteCriminalRecordUsecase:
    def __init__(self,repo_criminal_record : ICriminalRecordRepository):
        self.repo_criminal_record = repo_criminal_record

    def __call__(self, id:str) -> CriminalRecord:
        return self.repo_criminal_record.delete_criminal_record(id)
