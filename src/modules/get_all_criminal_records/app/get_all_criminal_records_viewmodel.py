from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME


class GetAllCriminalRecordsViewModel:
    id: str
    type_crime: TYPE_CRIME
    is_in_jail: bool
    danger_score: int
    criminal: Criminal


    def __init__(self, list_criminal_records : list[CriminalRecord]) -> None:
        self.list = list_criminal_records

    def to_dict(self):
        array = []
        for item in self.list:
            array.append({
                "criminal_record": {
                    "record_id": item.id,
                    "is_in_jail": item.is_in_jail,
                    "danger_score": item.danger_score,
                    "criminal": item.criminal.to_dict()
                },
                "message": "Criminal record was created"
            })
        return array
