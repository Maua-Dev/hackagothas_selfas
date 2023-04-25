from src.modules.update_criminal_record.app.update_criminal_record_usecase import UpdateCriminalRecordUseCase
from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewmodel
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, OK, NotFound


class UpdateCriminalRecordController:#a

    def __init__(self, update_criminal_record_use_case: UpdateCriminalRecordUseCase):
        self.update_criminal_record_use_case = update_criminal_record_use_case

    def __call__(self, request: IRequest):
        try:
            if request.data.get("record_id_to_update") is None:
                raise MissingParameters("record_to_update")

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
                GENDER(request.data.get("criminal_gender")),
                FAVORITE_REGION(request.data.get("criminal_favorite_region")),
                request.data.get("criminal_powers"),
            )

            new_criminal_record_value = CriminalRecord(request.data.get("record_id_to_update"),
                                             TYPE_CRIME(request.data.get("type_crime")),
                                             bool(request.data.get("is_in_jail")),
                                             int(request.data.get("danger_score")),
                                             criminal
                                             )

            response = self.update_criminal_record_use_case(request.data.get("record_id_to_update"), new_criminal_record_value)
            viewModel = UpdateCriminalRecordViewmodel(response)

            return OK(viewModel.to_dict())

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
