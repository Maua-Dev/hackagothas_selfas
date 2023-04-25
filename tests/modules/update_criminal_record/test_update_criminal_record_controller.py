from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.modules.update_criminal_record.app.update_criminal_record_controller import UpdateCriminalRecordController
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_UpdateCriminalRecordController:
    repo = CriminalRecordRepositoryMock()
    usecase = UpdateCriminalRecordUseCase(repo)
    controller = UpdateCriminalRecordController(update_criminal_record_use_case=usecase)
    id_that_exists = repo.criminal_records_list[0].id

    def test_update_missing_id_to_update(self):
        request = HttpRequest(body={
            # "record_id_to_update" : self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_is_in_jail_value(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            # "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_danger_score_value(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            # "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_name_value(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            # "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_id_value(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            # "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_description(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            # "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_gender(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            # "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_favorite_region(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            # "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_missing_criminal_powers(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            # "criminal_powers": "Bela oratoria"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_criminal_record_when_crime_id_is_missing(self):
        request = HttpRequest(body={
            "record_id_to_update": "um id que não existe",
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Belaoratoria",
            # "criminal_crimes_id": "32",
            "criminal_crimes_type": "MURDER"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_criminal_record_when_crime_type_is_missing(self):
        request = HttpRequest(body={
            "record_id_to_update": "um id que não existe",
            "is_in_jail": True,
            "danger_score": 81,
            "criminal_name": "Charada",
            "criminal_id": "420",
            "criminal_description": "Umas charadas muito loucas",
            "criminal_gender": "MALE",
            "criminal_favorite_region": "WAYNE_TOWER",
            "criminal_powers": "Belaoratoria",
            "criminal_crimes_id": "32",
            # "criminal_crimes_type": "MURDER"
        })

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_criminal_record_when_score_is_out_of_interval(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
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

        response = self.controller(request)
        assert response.status_code == 400

    def test_update_criminal_record_when_id_doesnt_exists(self):
        request = HttpRequest(body={
            "record_id_to_update": "um id que não existe",
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

        response = self.controller(request)
        assert response.status_code == 404

    def test_update_criminal_record_when_everything_is_fine(self):
        request = HttpRequest(body={
            "record_id_to_update": self.id_that_exists,
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

        response = self.controller(request)
        assert response.status_code == 200
