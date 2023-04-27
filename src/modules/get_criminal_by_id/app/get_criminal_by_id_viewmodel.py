from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER


class GetCriminalByIdViewModel:
    name: str
    criminal_id: str
    description: str
    gender: GENDER
    favorite_region: FAVORITE_REGION
    powers: str
    crime: Crime
    
    def __init__(self, criminal: Criminal) -> None:
        self.name = criminal.name
        self.criminal_id = criminal.criminal_id
        self.description = criminal.description
        self.gender = criminal.gender
        self.favorite_region = criminal.favorite_region
        self.powers = criminal.powers
        self.crime = Crime(criminal.crime.id, criminal.crime.type_crime)

    def to_dict(self):
        return {
            "criminal":{
                "criminal_id": self.criminal_id,
                "name":self.name,
                "description":self.description,
                "gender":self.gender.value,
                "favorite_region":self.favorite_region.value,
                "powers":self.powers,
                "crime":{
                    "id": self.crime.id,
                    "type_crime":self.crime.type_crime.value
                }
            },
            "message": "the criminal was retrieved successfully"
        }
