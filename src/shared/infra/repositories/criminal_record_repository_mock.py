from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION


class CriminalRecordRepositoryMock(ICriminalRecordRepository):

    criminal_record: list[CriminalRecord]

    criminal: list[Criminal]

    def __init__(self):
        self.criminals = [
            Criminal(name="Coringa", id="oiue281u", description="palhaco",
                     gender=GENDER.NON_BINARY, favorite_region=FAVORITE_REGION.WAYNE_TOWER, powers="risadinha")
        ]
        self.criminal_records = [
            CriminalRecord(id="jdiqhihq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
                           is_in_jail=False, danger_score=94, criminal=self.criminals[0])
        ]

    def create_criminal_record(self, criminal_record: CriminalRecord) -> CriminalRecord:
        self.criminal_records.append(criminal_record)
        return self.criminal_records
