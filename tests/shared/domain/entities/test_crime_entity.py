import pytest

from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.helpers.errors.domain_errors import EntityError

criminal = Criminal("Duez", "42", "Deuz gamer", GENDER.MALE, FAVORITE_REGION.GRANT_PARK, "Os mesmos do homem-aranha")

def test_crime_entity_instantiation():
    Crime("42", TYPE_CRIME.MURDER, criminal)

def test_crime_entity_id_is_not_string():
    with pytest.raises(EntityError):
        Crime(42, TYPE_CRIME.MURDER, criminal)

def test_crime_entity_type_crime_is_not_enum():
    with pytest.raises(EntityError):
        Crime("42", "Murder",  criminal)

def test_crime_entity_criminal_is_not_criminal():
    with pytest.raises(EntityError):
        Crime("42", "Murder",  "Um criminoso ai")
