from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class CreateCriminalRecordViewmodel:
    id: str
    type_crime: TYPE_CRIME
    is_in_jail: bool
    danger_score: int
    criminal: Criminal

    # criminal_record: CriminalRecord

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
                "criminal": self.criminal.to_dict()
            },
            "message": "Criminal record was created"
        }
