from src.modules.get_criminal_by_id.app.get_criminal_by_id_viewmodel import GetCriminalByIdViewModel
from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class TestGetCriminalByIdViewmodel:
    def test_get_criminal_by_id_viewmodel(self):
        criminal = Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do miranha", Crime("444", TYPE_CRIME.MURDER))

        viewmodel = GetCriminalByIdViewModel(criminal)

        response = viewmodel.to_dict()

        assert type(response) is dict
        assert response["criminal"]["criminal_id"] == criminal.criminal_id
        assert response["criminal"]["name"] == criminal.name
        assert response["criminal"]["description"] == criminal.description
        assert response["criminal"]["gender"] == criminal.gender.value
        assert response["criminal"]["favorite_region"] == criminal.favorite_region.value
        assert response["criminal"]["powers"] == criminal.powers
        assert response["criminal"]["crime"]["id"] == criminal.crime.id
        assert response["criminal"]["crime"]["type_crime"] == criminal.crime.type_crime.value
