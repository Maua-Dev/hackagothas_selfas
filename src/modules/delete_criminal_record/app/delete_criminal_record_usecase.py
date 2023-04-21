from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError


class DeleteCriminalRecordUsecase:
    def __init__(self,repo_criminal_record : ICriminalRecordRepository):
        self.repo_criminal_record = repo_criminal_record

    def __call__(self, criminal_record_id : str) -> CriminalRecord:

        if type(criminal_record_id) != str:
            raise EntityError("criminal_record_id")

        return self.repo_criminal_record.delete_criminal_record(criminal_record_id)
