import pytest

from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_controller import GetCriminalRecordByIdController
from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_use_case import GetCriminalRecordByIdUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_GetCriminalRecordByIdController:
    controller = GetCriminalRecordByIdController(GetCriminalRecordByIdUseCase(CriminalRecordRepositoryMock()))

    def test_get_criminal_record_when_id_is_missing(self):
        request = HttpRequest(body={
            # Vazio
        })

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_criminal_record_when_id_is_not_string(self):
        request = HttpRequest(body={
            "criminal_record_id": 42
        })

        response = self.controller(request)

        assert response.status_code == 400

    def test_get_criminal_record_should_return_not_found(self):
        request = HttpRequest(body={
            "criminal_record_id": "Um id que nao existe"
        })

        response = self.controller(request)

        assert response.status_code == 404
