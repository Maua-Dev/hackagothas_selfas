from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository


class GetAllCriminalRecordsUsecase:
    def __init__(self, repo: ICriminalRecordRepository) -> list[CriminalRecord]:
        self.repo = repo

    def __call__(self):
        return self.repo.get_all_criminal_records()
