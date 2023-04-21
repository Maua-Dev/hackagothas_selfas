from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestDeleteCriminalRecordUsecase:
    def test_delete_criminal_record_usecase(self):
        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        response = usecase("jdiqhihq")

        expected = []

        assert response == expected
