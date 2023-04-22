from src.modules.get_all_criminal_records.app.get_all_criminal_records_controller import GetAllCriminalRecordsController
from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.modules.get_all_criminal_records.app.get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewModel
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestGetAllCriminalRecordsController:
    def test_get_all_criminal_records_controller(self):
        repo = CriminalRecordRepositoryMock()

        usecase = GetAllCriminalRecordsUsecase(repo)

        viewmodel = GetAllCriminalRecordsViewModel(usecase)

        request = HttpRequest(body={})

        response = GetAllCriminalRecordsController(request)

        assert response.status_code == 200
