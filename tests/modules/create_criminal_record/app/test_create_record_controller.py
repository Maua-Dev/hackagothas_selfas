import pytest

from src.modules.create_criminal_record.app.create_criminal_record_controller import CreateRecordController
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestCreateRecordController:
    repoMock = CriminalRecordRepositoryMock()
    useCase = CreateCriminalRecordUsecase(repoMock)
    createRecordController = CreateRecordController(useCase)

    def test_controller_should_create_correctly(self):
        request = HttpRequest(body={
            "record_id": "42",
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Belaoratoria",
            "criminal_crimes_id": "32",
            "criminal_crimes_type": "MURDER"
        })

        response = self.createRecordController(request)
        assert response.status_code == 201

    def test_controller_should_throw_a_error_when_score_is_not_valid(self):
        request = HttpRequest(body={
            "record_id": "42",
            "is_in_jail": True,
            "danger_score": 8001,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Belaoratoria",
            "criminal_crimes_id": "32",
            "criminal_crimes_type": "MURDER"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_record_id(self):
        request = HttpRequest(body={
            # "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": 8001,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria",

        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_type_crime(self):
        request = HttpRequest(body={
            "record_id": "42",
            # "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_is_in_jail(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            # "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_danger_score(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            # "danger_score": 8001,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_name(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            # "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_id(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            # "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_description(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            # "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_gender(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            # "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_region(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            # "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

    def test_controller_missing_criminal_powers(self):
        request = HttpRequest(body={
            "record_id": "42",
            "type_crime": "FUCK_BOY",
            "is_in_jail": True,
            "danger_score": "8001",
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            # "criminal_powers": "Bela oratoria"
        })

        response = self.createRecordController(request)
        assert response.status_code == 400

