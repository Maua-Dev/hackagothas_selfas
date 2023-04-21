import pytest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class Test_CriminalRecordRepositoryMock:
    def test_create_criminal_record(self):
        repo = CriminalRecordRepositoryMock()

        length_before = len(repo.criminal_records)

        repo.create_criminal_record(criminal_record=repo.criminal_records[0])

        length_after = len(repo.criminal_records)

        assert length_after == length_before + 1

    def test_delete_criminal_record(self):
        repo = CriminalRecordRepositoryMock()

        length_before = len(repo.criminal_records)

        repo.delete_criminal_record(id=repo.criminal_records[0].id)

        length_after = len(repo.criminal_records)

        assert length_after == length_before - 1

    def test_delete_criminal_record_when_id_doesnt_exists(self):
        with pytest.raises(NoItemsFound):
            repo = CriminalRecordRepositoryMock()

            id_nao_existente = "id_nao_existente"

            repo.delete_criminal_record(id=id_nao_existente)

            
