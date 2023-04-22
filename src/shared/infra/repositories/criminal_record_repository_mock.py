from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class CriminalRecordRepositoryMock(ICriminalRecordRepository):

    criminal_records_list: list[CriminalRecord]

    criminals_list: list[Criminal]

    def __init__(self):
        self.criminals_list = [
            Criminal(name="Coringa", criminal_id="oiue281u", description="palhaco",
                     gender=GENDER.NON_BINARY, favorite_region=FAVORITE_REGION.WAYNE_TOWER, powers="risadinha")
        ]
        self.criminal_records_list = [
            CriminalRecord(id="jdiqhihq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
                           is_in_jail=False, danger_score=94, criminal=self.criminals_list[0])
        ]

    def create_criminal_record(self, criminal_record: CriminalRecord) -> CriminalRecord:
        self.criminal_records_list.append(criminal_record)
        return criminal_record

    def get_criminal_record_by_id(self, id_to_search: str) -> CriminalRecord:
        for record in self.criminal_records_list:
            if record.id == id_to_search:
                return record

        raise NoItemsFound("Criminal Record ID")

    def get_all_criminal_records(self) -> list[CriminalRecord]:
        if(len(self.criminal_records_list) == 0):
            raise NoItemsFound("No Criminal Record found")

        return self.criminal_records_list











