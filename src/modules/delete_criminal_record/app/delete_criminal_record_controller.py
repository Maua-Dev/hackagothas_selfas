from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteCriminalRecordController:
    def __init__(self, delete_criminal_record_usecase: CriminalRecord):

        self.delete_criminal_record_usecase = delete_criminal_record_usecase

    def __call__(self, request: IRequest):

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
            
            return OK(viewmodel.to_dict())
        
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

        
    