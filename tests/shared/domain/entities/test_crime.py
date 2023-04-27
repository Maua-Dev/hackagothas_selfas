import pytest
from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.helpers.errors.domain_errors import EntityError

class TestCrime:
    def test_crime(self):
        crime = Crime("42",TYPE_CRIME.CRIME_AGAINST_SELFAS_THE_BEST_PROJECT)
        assert type(crime) is Crime

    def test_crime_entity_id_is_not_string(self):
        with pytest.raises(EntityError):
            Crime(42, TYPE_CRIME.MURDER)

    def test_crime_entity_type_crime_is_not_enum(self):
        with pytest.raises(EntityError):
            Crime("42", "Murder")
