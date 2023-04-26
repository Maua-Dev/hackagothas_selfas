from src.modules.get_criminal_by_id.app.get_criminal_by_id_controller import GetCriminalByIdController
from src.modules.get_criminal_by_id.app.get_criminal_by_id_usecase import GetCriminalByIdUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock


class TestGetCriminalByIdController:
    def test_get_criminal_by_id(self):
        repo = CriminalRepositoryMock()

        usecase = GetCriminalByIdUsecase(repo)

        controller = GetCriminalByIdController(usecase)


        request = HttpRequest(body={
            "record_id" : "oiue281u"
        })

        response = controller(request)
        assert response.status_code == 200

    def test_get_criminal_by_id_is_wrong_type(self):
        repo = CriminalRepositoryMock()

        usecase = GetCriminalByIdUsecase(repo)

        controller = GetCriminalByIdController(usecase)


        request = HttpRequest(body={
            "record_id" : 40
        })

        response = controller(request)
        assert response.status_code == 400

    def test_get_criminal_by_id_is_non_existent(self):
        repo = CriminalRepositoryMock()

        usecase = GetCriminalByIdUsecase(repo)

        controller = GetCriminalByIdController(usecase)


        request = HttpRequest(body={
            "record_id" : "aaaaaaaa"
        })

        response = controller(request)
        assert response.status_code == 404
