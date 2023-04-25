from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class CreateCriminalRecordViewmodel:
    id: str
    is_in_jail: bool
    danger_score: int
    criminal: Criminal

    def __init__(self, criminal_record: CriminalRecord):
        self.id = criminal_record.id
        self.is_in_jail = criminal_record.is_in_jail
        self.danger_score = criminal_record.danger_score
        self.criminal = criminal_record.criminal

    def to_dict(self):
        return {
            "criminal_record": {
                "record_id": self.id,
                "is_in_jail": self.is_in_jail,
                "danger_score": self.danger_score,
                # "criminal": self.criminal.to_dict()
                "criminal": {
                    "name": self.criminal.name,
                    "id": self.criminal.criminal_id,
                    "description": self.criminal.description,
                    "gender": self.criminal.gender.value,
                    "favorite_region": self.criminal.favorite_region.value,
                    "power": self.criminal.powers,
                    # "crime": self.criminal.crime.to_dict()
                    "crime_id": self.criminal.crime.id,
                    "crime_type_crime":self.criminal.crime.type_crime.value
                }
            },
            "message": "Criminal record was created"
        }
