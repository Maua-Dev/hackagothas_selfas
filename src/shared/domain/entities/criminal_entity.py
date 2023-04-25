from abc import ABC
from src.shared.domain.entities.crime_entity import Crime
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION


class Criminal(ABC):
    name: str
    criminal_id: str
    description: str
    gender: GENDER
    favorite_region: FAVORITE_REGION
    powers: str
    crime: Crime

    def __init__(self, name: str, criminal_id: str, description: str, gender: GENDER, favorite_region: FAVORITE_REGION,
                 powers: str, crime: Crime):
        if type(name) != str:
            raise EntityError("name")
        self.name = name

        if type(criminal_id) != str:
            raise EntityError("id")
        self.criminal_id = criminal_id

        if type(description) != str:
            raise EntityError("description")
        self.description = description

        if type(gender) != GENDER:
            raise EntityError("gender")
        self.gender = gender

        if type(favorite_region) != FAVORITE_REGION:
            raise EntityError("favorite_region")
        self.favorite_region = favorite_region

        if type(powers) != str:
            raise EntityError("powers")
        self.powers = powers

        if type(crime) != Crime:
            raise EntityError("crime")
        self.crime = crime

    @staticmethod
    def validate_name(name: str) -> bool:
        if (type(name) != str):
            return False
        if (len(name) < 2):
            return False
        return True

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.criminal_id,
            "description": self.description,
            "gender": self.gender.value,
            "favorite_region": self.favorite_region.value,
            "power": self.powers,
            "crime": self.crime.to_dict()
            # "crime_id": self.crime.id,
            # "type_crime":self.crime.type_crime.value
        }
