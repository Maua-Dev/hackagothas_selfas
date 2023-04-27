from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository


class GetCriminalByIdUsecase:

    def __init__(self, repository:ICriminalRepository):
        self.repo = repository

    def __call__(self, record_id: str):
        return self.repo.get_criminal_by_id(record_id)
