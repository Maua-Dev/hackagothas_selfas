from src.modules.create_criminal_record.app.create_criminal_record_controller import CreateRecordController
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse

def create_criminal_record_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = CreateCriminalRecordUsecase(repo)
    controller = CreateRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()