from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class UpdateCriminalRecordUseCase:
    def __init__(self, repo_criminal_record: ICriminalRecordRepository):
        self.repo_criminal_record = repo_criminal_record

    def __call__(self, id_to_update: str, new_record_value: CriminalRecord):
        if id_to_update != new_record_value.id:
            raise ForbiddenAction("new record value's id must be equal to id to update")

        if not CriminalRecord.validade_danger_score(new_record_value.danger_score):
            raise EntityError("danger_score")

        return self.repo_criminal_record.update_criminal_record(id_to_update, new_record_value)
