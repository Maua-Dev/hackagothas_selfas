from src.modules.create_criminal_record.app.create_criminal_record_view_model import CreateCriminalRecordViewmodel
from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class Test_CreateCriminalRecordViewmodel:
    def test_convert_to_dictionary(self):
        criminal = Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do miranha", Crime("42", TYPE_CRIME.MURDER))
        criminalRecord = CriminalRecord("42", True, 8001, criminal)

        viewModel = CreateCriminalRecordViewmodel(criminalRecord)

        response = viewModel.to_dict()

        assert type(response) == dict
        assert response["criminal_record"]["record_id"] == criminalRecord.id
        assert response["criminal_record"]["is_in_jail"] == criminalRecord.is_in_jail
        assert response["criminal_record"]["danger_score"] == criminalRecord.danger_score
        assert response["criminal_record"]["criminal"] == criminalRecord.criminal.to_dict()

        assert response["criminal_record"]["criminal"]["name"] == "Duez"
        assert response["criminal_record"]["criminal"]["id"] == "42"
        assert response["criminal_record"]["criminal"]["description"] == "Deuz Gamer"
        assert response["criminal_record"]["criminal"]["gender"] == "MALE"
        assert response["criminal_record"]["criminal"]["favorite_region"] == "CITY_HALL"
        assert response["criminal_record"]["criminal"]["power"] == "Os mesmos do miranha"
        # assert response["criminal_record"]["criminal"]["crime"] == criminalRecord.criminal.crime.to_dict()
        assert response['criminal_record']['criminal']['crime_id'] == "42"
        assert response['criminal_record']['criminal']['crime_type_crime'] == "MURDER"

        print(response['criminal_record']['criminal'])
        assert response["message"] == "Criminal record was created"


