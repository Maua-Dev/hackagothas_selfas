from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_controller import GetCriminalRecordByIdController
from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_use_case import GetCriminalRecordByIdUseCase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def get_criminal_record_by_id_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = GetCriminalRecordByIdUseCase(repo)
    controller = GetCriminalRecordByIdController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse
