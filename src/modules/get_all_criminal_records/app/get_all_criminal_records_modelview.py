from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class GetAllCriminalRecordsModelview:
    id: str
    type_crime: TYPE_CRIME
    is_in_jail: bool
    danger_score: int
    criminal: Criminal


    def __init__(self, list : list[CriminalRecord]) -> None:
        self.list = []

    def to_dict(self):
        array = []
        for item in self.list:
            array.append({
                "criminal_record": {
                "record_id": item.id,
                "type_crime": item.type_crime,
                "is_in_jail": item.is_in_jail,
                "danger_score": item.danger_score,
                "criminal": item.criminal.to_dict()
                },
                "message": "Criminal record was created"
            })
        return array
