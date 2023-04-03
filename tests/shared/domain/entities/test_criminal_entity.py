import pytest

from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.helpers.errors.domain_errors import EntityError


def test_criminal_instantiation():
    Criminal("Lucas Duez", "42", "Deuz gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do homem-aranha")

def test_criminal_name_is_not_string():
    with pytest.raises(EntityError):
        Criminal(25, "42", "Deuz gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do homem-aranha")

def test_criminal_id_is_not_string():
    with pytest.raises(EntityError):
        Criminal("Duez", 42, "Deuz gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do homem-aranha")

def test_criminal_description_is_not_string():
    with pytest.raises(EntityError):
        Criminal("Duez", "42", 25, GENDER.MALE, FAVORITE_REGION.CITY_HALL, "Os mesmos do homem-aranha")

def test_criminal_gender_is_not_enum():
    with pytest.raises(EntityError):
        Criminal("Duez", "42", "Deuz Gamer", "Male", FAVORITE_REGION.CITY_HALL, "Os mesmos do homem-aranha")

def test_criminal_region_is_not_enum():
    with pytest.raises(EntityError):
        Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, "City Hall",  "Os mesmos do homem-aranha")

def test_criminal_powers_is_not_string():
    with pytest.raises(EntityError):
        Criminal("Duez", "42", "Deuz Gamer", GENDER.MALE, FAVORITE_REGION.CITY_HALL, 8001)
