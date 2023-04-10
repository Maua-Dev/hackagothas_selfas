import pytest
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock

class Test_CriminalRecordRepositoryMock:
    def test_create_criminal_record(self):
        repo = CriminalRecordRepositoryMock()

        length_before = len(repo.criminal_records_list)

        repo.create_criminal_record(criminal_record=repo.criminal_records_list[0])

        length_after = len(repo.criminal_records_list)

        assert length_after == length_before + 1

    def test_get_criminal_record_by_id_when_id_exists(self):
        repo = CriminalRecordRepositoryMock()

        id_to_search = repo.criminal_records_list[0].id

        response = repo.get_criminal_record_by_id(id_to_search)
        expected = repo.criminal_records_list[0]

        assert response is expected

    def test_get_criminal_record_by_id_when_id_doesnt_exists(self):
        with pytest.raises(NoItemsFound):
            repo = CriminalRecordRepositoryMock()
            id_to_search = "Um id que nao existe"
            response = repo.get_criminal_record_by_id(id_to_search)


