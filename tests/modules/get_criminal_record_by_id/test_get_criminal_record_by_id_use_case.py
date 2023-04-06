from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_use_case import GetCriminalRecordByIdUseCase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestGetCriminalRecordByIdUseCase:
    def test_get_criminal_record_by_id_use_case(self):
        repo = CriminalRecordRepositoryMock()
        use_case = GetCriminalRecordByIdUseCase(repo)
        response = use_case("jdiqhihq")
        expected = repo.criminal_records_list[0]

        assert response == expected