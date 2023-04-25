from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestDeleteCriminalRecordUsecase:
    def test_delete_criminal_record_usecase(self):
        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        id_to_search = "jdiqhihq"

        expected = repo.criminal_records_list[0]
        repo_list_length_before = len(repo.criminal_records_list)

        response = usecase(id_to_search)

        repo_list_length_after = len(repo.criminal_records_list)

        assert response == expected
        assert repo_list_length_after == repo_list_length_before - 1
