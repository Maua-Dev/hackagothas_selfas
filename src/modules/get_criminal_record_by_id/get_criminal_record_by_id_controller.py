from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_use_case import GetCriminalRecordByIdUseCase
from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_view_model import GetCriminalRecordByIdViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK, InternalServerError, NotFound


class GetCriminalRecordByIdController:
    def __init__(self, get_criminal_use_case: GetCriminalRecordByIdUseCase):
        self.get_criminal_use_case = get_criminal_use_case

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

            criminal_record = self.get_criminal_use_case(request.data.get("criminal_record_id"))
            view_model = GetCriminalRecordByIdViewmodel(criminal_record)
            return OK(view_model.to_dict())

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
