from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase
from src.modules.create_criminal_record.app.create_criminal_record_view_model import CreateCriminalRecordViewModel
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError


class CreateRecordController:
    def __init__(self, create_record_use_case: CreateCriminalRecordUsecase):
        self.create_record_use_case = create_record_use_case

    def __call__(self, request: IRequest):
        try:
            if request.data.get("record_id") is None:
                raise MissingParameters("record_id")

            if request.data.get("type_crime") is None:
                raise MissingParameters("type_crime")

            if request.data.get("is_in_jail") is None:
                raise MissingParameters("is_in_jail")

            if request.data.get("danger_score") is None:
                raise MissingParameters("danger_score")

            if request.data.get("criminal_name") is None:
                raise MissingParameters("criminal_name")

            if request.data.get("criminal_id") is None:
                raise MissingParameters("criminal_id")

            if request.data.get("criminal_description") is None:
                raise MissingParameters("criminal_description")

            if request.data.get("criminal_gender") is None:
                raise MissingParameters("criminal_gender")

            if request.data.get("criminal_favorite_region") is None:
                raise MissingParameters("criminal_favorite_region")

            if request.data.get("criminal_powers") is None:
                raise MissingParameters("criminal_powers")

            criminal = Criminal(
                request.data.get("criminal_name"),
                request.data.get("criminal_id"),
                request.data.get("criminal_description"),
                request.data.get("criminal_gender"),
                request.data.get("criminal_favorite_region"),
                request.data.get("criminal_powers"),
            )

            criminal_record = CriminalRecord(request.data.get("record_id"),
                                             request.data.get("type_crime"),
                                             request.data.get("is_in_jail"),
                                             request.data.get("danger_score"),
                                             criminal
                                             )

            response: CriminalRecord = self.create_record_use_case(criminal_record.danger_score, criminal_record)
            viewModel = CreateCriminalRecordViewModel(response)

            return Created(viewModel.convert_to_dictionary())

        except MissingParameters as e:
            return BadRequest(body=e)

        except EntityError as e:
            return BadRequest(body=e.message)

        except Exception as e:
            return InternalServerError(body=e.args[0])





