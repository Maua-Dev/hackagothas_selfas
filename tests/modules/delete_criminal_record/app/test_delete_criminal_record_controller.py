from src.modules.delete_criminal_record.app.delete_criminal_record_controller import DeleteCriminalRecordController
from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestDeleteCriminalRecordController:
    def test_delete_criminal_record_controller(self):
        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(body={
            "criminal_record_id": repo.criminal_records[0].id
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "Criminal record was deleted successfully"

    def test_delete_criminal_record_when_id_is_missing(self):

        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(body={})

        response = controller(request)

        assert response.status_code == 400
    
    def test_delete_criminal_record_when_id_is_not_string(self):
        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(body={
            "criminal_record_id":213
        })

        response = controller(request)

        assert response.status_code == 400

    def test_get_criminal_record_should_return_not_found(self):
        repo = CriminalRecordRepositoryMock()

        usecase = DeleteCriminalRecordUsecase(repo)

        controller = DeleteCriminalRecordController(usecase)

        request = HttpRequest(body={
            "criminal_record_id": "id_que_nao_existe"
        })

        response = controller(request)

        assert response.status_code == 404

