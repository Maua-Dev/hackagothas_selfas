import pytest

from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.helpers.errors.domain_errors import EntityError

criminal = Criminal("Duez", "42", "Deuz gamer", GENDER.MALE, FAVORITE_REGION.GRANT_PARK, "Os mesmos do homem-aranha")

def test_criminal_record_instantiation():
    CriminalRecord("42", TYPE_CRIME.MURDER, True, 8001, criminal)


def test_id_is_not_string():
    with pytest.raises(EntityError):
        CriminalRecord(42, TYPE_CRIME.MURDER, True, 8001, criminal)

def test_type_crime_is_not_enum():
    with pytest.raises(EntityError):
        CriminalRecord("42", "Murder", True, 8001, criminal)

def test_is_in_jail_is_not_boolean():
    with pytest.raises(EntityError):
        CriminalRecord("42", TYPE_CRIME.MURDER, "true", 8001, criminal)

def test_danger_score_is_not_integer():
    with pytest.raises(EntityError):
        CriminalRecord("42", TYPE_CRIME.MURDER, True, "mais de oito mil", criminal)

def test_criminal_is_not_criminal_type():
    with pytest.raises(EntityError):
        CriminalRecord("42", TYPE_CRIME.MURDER, True, 8001, "Eu sou um criminoso")
