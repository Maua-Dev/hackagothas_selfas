from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.modules.get_all_criminal_records.app.get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewModel
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, OK, InternalServerError, NotFound


class GetAllCriminalRecordsController:
    def __init__(self, list : GetAllCriminalRecordsUsecase) -> list[CriminalRecord]:
        self.get_all_criminal_records = list

    def __call__(self, request : HttpRequest):
        try:
            criminal_record = self.get_all_criminal_records()

            viewmodel = GetAllCriminalRecordsViewModel(criminal_record)

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
        
