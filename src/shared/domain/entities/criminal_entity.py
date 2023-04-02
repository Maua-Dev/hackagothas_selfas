from abc import ABC
from helpers.errors.domain_errors import EntityError
from enums.gender_enum import GENDER
from enums.favorite_region_enum import FAVORITE_REGION


class Criminal(ABC):
    name: str
    id: str
    description: str
    gender: GENDER
    favorite_region: FAVORITE_REGION
    powers: str

    def __init__(self, name: str, id: str, description: str, gender: GENDER, favorite_region: FAVORITE_REGION, powers: str):
        if type(name) != str:
            raise EntityError("name")
        self.name = name

        if type(id) != str:
            raise EntityError("id")
        self.id = id

        if type(description) != str:
            raise EntityError("description")
        self.description = description

        if type(gender) != GENDER:
            raise EntityError("gender")
        self.gender = GENDER

        if type(favorite_region) != FAVORITE_REGION:
            raise EntityError("favorite_region")
        self.favorite_region = FAVORITE_REGION

        if type(powers) != str:
            raise EntityError("powers")
        self.powers = powers
