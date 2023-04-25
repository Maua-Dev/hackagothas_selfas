from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.repositories.criminal_record_repository_interface import ICriminalRecordRepository
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock


class CriminalRecordRepositoryMock(ICriminalRecordRepository):
    criminal_records_list: list[CriminalRecord]

    criminals_list: list[Criminal]

    def __init__(self):

        repo_criminal = CriminalRepositoryMock()
        self.criminals_list = repo_criminal.criminals_list
        
        self.criminal_records_list = [
            CriminalRecord(id="jdiqhihq",
                           is_in_jail=False, danger_score=94, criminal=self.criminals_list[0]),
            CriminalRecord(id="asadwa",
                           is_in_jail=True, danger_score=27, criminal=self.criminals_list[1])
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
        if (len(self.criminal_records_list) == 0):
            raise NoItemsFound("No Criminal Record found")

        return self.criminal_records_list

    def update_criminal_record(self, id_to_update: str, new_record_value: CriminalRecord) -> CriminalRecord:
        for i in range(len(self.criminal_records_list)):
            if self.criminal_records_list[i].id == id_to_update:
                self.criminal_records_list[i] = new_record_value
                return self.criminal_records_list[i]

        raise NoItemsFound("Criminal Record ID")

    def delete_criminal_record(self, id) -> CriminalRecord:
        for index, criminal in enumerate(self.criminal_records_list):
            if criminal.id == id:
                return self.criminal_records_list.pop(index)

        raise NoItemsFound("Criminal Record ID")
