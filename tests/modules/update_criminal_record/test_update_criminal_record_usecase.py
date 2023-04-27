import pytest

from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


#A
class Test_UpdateCriminalRecordUseCase:
    repo = CriminalRecordRepositoryMock()
    use_case = UpdateCriminalRecordUseCase(repo)

    def test_update_criminal_record_usecase(self):
        id_to_update = self.repo.criminal_records_list[0].id
        new_record_value = self.repo.criminal_records_list[0]

        new_record_value.criminal.name = "Lucas Duez"

        self.use_case(id_to_update, new_record_value)

        assert self.repo.criminal_records_list[0] == new_record_value

    def test_update_criminal_record_when_id_does_not_exist(self):
        id_to_update = "Um id que nao existe"
        record = self.repo.criminal_records_list[0]

        with pytest.raises(ForbiddenAction):
            self.use_case(id_to_update, record)

    def test_update_criminal_record_when_danger_score_is_invalid(self):
        id_to_update = self.repo.criminal_records_list[0].id
        new_record_value = self.repo.criminal_records_list[0]
        new_record_value.danger_score = -90

        with pytest.raises(EntityError):
            self.use_case(id_to_update, new_record_value)
