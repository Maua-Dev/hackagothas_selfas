from src.modules.delete_criminal_record.app.delete_criminal_record_viewmodel import DeleteCriminalRecordViewmodel
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class TestDeleteCriminalRecordViewmodel:
    def test_delete_criminal_record_usecase(self):
        criminal = Criminal("Bitu","234","Matador de pomba",GENDER.MALE,FAVORITE_REGION.ROBBINSVILLE,"revolver no pombo")
        
        criminal_record = CriminalRecord("234", TYPE_CRIME.CRIME_AGAINST_SELFAS_THE_BEST_PROJECT, True, 90, criminal)

        viewmodel = DeleteCriminalRecordViewmodel(criminal_record)

        response = viewmodel.to_dict()

        assert type(response) == dict
        assert response["criminal_record"]["record_id"] == criminal_record.id
        assert response["criminal_record"]["type_crime"] == criminal_record.type_crime.value
        assert response["criminal_record"]["is_in_jail"] == criminal_record.is_in_jail
        assert response["criminal_record"]["danger_score"] == criminal_record.danger_score
        assert response["criminal_record"]["criminal"] == criminal_record.criminal.to_dict()
        assert response["message"] == "Criminal record was deleted successfully"
