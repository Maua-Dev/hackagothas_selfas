from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository


class GetCriminalRecordByIdUseCase:
    def __init__(self, repository: ICriminalRecordRepository):
        self.repository = repository

    def __call__(self, record_id: str):
        return self.repository.get_criminal_record_by_id(record_id)

