from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestGetAllCriminalRecords:
    def test_get_all_criminal_records(self):
        repo = CriminalRecordRepositoryMock()

        usecase = GetAllCriminalRecordsUsecase(repo)

        response = usecase()

        expected = repo.get_all_criminal_records()

        assert response == expected
