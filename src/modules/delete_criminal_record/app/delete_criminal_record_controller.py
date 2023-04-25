from src.modules.delete_criminal_record.app.delete_criminal_record_usecase import DeleteCriminalRecordUsecase
from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse


class DeleteCriminalRecordController:
    def __init__(self, usecase: DeleteCriminalRecordUsecase):

        self.delete_criminal_record_usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:

        try:

            if request.data.get("criminal_record_id") is None:
                raise MissingParameters("criminal_record_id")
            
            if type(request.data.get("criminal_record_id")) != str:
                raise WrongTypeParameter(
                    fieldName="criminal_record_str",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get('criminal_record_id').__class__.__name__
                )
            
            criminal_record = self.delete_criminal_record_usecase(request.data.get("criminal_record_id"))

            viewmodel = DeleteCriminalRecordViewmodel(criminal_record)

            return OK(body=viewmodel.to_dict())
        
        except MissingParameters as e:
            return BadRequest(body=e.message)
        
        except EntityError as e:
            return BadRequest(body=e.message)

        except WrongTypeParameter as e:
            return BadRequest(body=e.message)

        except NoItemsFound as e:
            return NotFound(body=e.message)

        except Exception as e:
            return InternalServerError(body=e.args[0])

        
    