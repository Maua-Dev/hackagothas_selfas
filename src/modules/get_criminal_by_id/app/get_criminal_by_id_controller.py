from src.modules.get_criminal_by_id.app.get_criminal_by_id_usecase import GetCriminalByIdUsecase
from src.modules.get_criminal_by_id.app.get_criminal_by_id_viewmodel import GetCriminalByIdViewModel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK, InternalServerError, NotFound


class GetCriminalByIdController:
    def __init__(self, get_criminal_usecase) -> GetCriminalByIdUsecase:
        self.get_criminal_usecase = get_criminal_usecase

    def __call__(self, request : IRequest):
        try:
            if request.data.get("record_id") is None:
                raise MissingParameters("record_id")
            
            if type(request.data.get("record_id")) != str:
                raise WrongTypeParameter(
                    fieldName="record_id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get("record_id").__class__.__name__
                )
            
            criminal = self.get_criminal_usecase(request.data.get("record_id"))
            viewmodel = GetCriminalByIdViewModel(criminal)
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
