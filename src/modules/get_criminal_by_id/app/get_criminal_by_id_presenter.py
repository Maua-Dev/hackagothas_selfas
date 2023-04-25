from src.modules.get_criminal_by_id.app.get_criminal_by_id_controller import GetCriminalByIdController
from src.modules.get_criminal_by_id.app.get_criminal_by_id_usecase import GetCriminalByIdUsecase
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse


def get_criminal_by_id_presenter(event, context):
    repo = CriminalRepositoryMock()
    usecase = GetCriminalByIdUsecase(repo)
    controller = GetCriminalByIdController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse
    