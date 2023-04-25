from src.modules.update_criminal_record.app.update_criminal_record_viewmodel import UpdateCriminalRecordViewmodel
from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


#A
class Test_UpdateCriminalRecordByIdViewmodel:
    def test_convert_to_dictionary(self):
        criminal = Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do miranha", Crime("37", TYPE_CRIME.CRIME_AGAINST_SELFAS_THE_BEST_PROJECT))
        criminalRecord = CriminalRecord("42", True, 81, criminal)

        viewModel = UpdateCriminalRecordViewmodel(criminalRecord)

        response = viewModel.to_dict()

        assert type(response) == dict
        assert response["criminal_record"]["record_id"] == criminalRecord.id
        assert response["criminal_record"]["is_in_jail"] == criminalRecord.is_in_jail
        assert response["criminal_record"]["danger_score"] == criminalRecord.danger_score
        assert response["criminal_record"]["criminal"] == criminalRecord.criminal.to_dict()
        assert response["criminal_record"]["criminal"]["crime"] == criminalRecord.criminal.to_dict()["crime"]
        assert response["message"] == "the criminal record was updated successfully"


