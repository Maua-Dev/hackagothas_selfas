from src.modules.create_criminal_record.app.create_criminal_record_view_model import CreateCriminalRecordViewModel
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class Test_Create_Criminal_Record_View_Model:
    def test_convert_to_dictionary(self):
        criminal = Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do miranha")
        criminalRecord = CriminalRecord("42", TYPE_CRIME.MURDER, True, 8001, criminal)

        viewModel = CreateCriminalRecordViewModel(criminalRecord)

        response = viewModel.convert_to_dictionary()

        assert type(response) == dict
        assert response["record_id"] == criminalRecord.id
        assert response["type_crime"] == criminalRecord.type_crime
        assert response["is_in_jail"] == criminalRecord.is_in_jail
        assert response["danger_score"] == criminalRecord.danger_score
        assert response["criminal"] == criminalRecord.criminal.get_view_model()


