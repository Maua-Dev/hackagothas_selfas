from src.modules.update_criminal_record.app.update_criminal_record_controller import UpdateCriminalRecordController
from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
#a
def update_criminal_record_presenter(event, context):
    repo = CriminalRecordRepositoryMock()
    usecase = UpdateCriminalRecordUseCase(repo)
    controller = UpdateCriminalRecordController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
