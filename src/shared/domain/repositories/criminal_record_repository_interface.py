from abc import ABC, abstractmethod
from src.shared.domain.entities.criminal_record_entity import CriminalRecord


class ICriminalRecordRepository(ABC):

    @abstractmethod
    def create_criminal_record(self, criminal_record: CriminalRecord) -> CriminalRecord:
        pass

    @abstractmethod
    def get_criminal_record_by_id(self, id_to_search: str) -> CriminalRecord:
        pass

    @abstractmethod
    def get_all_criminal_records(self) -> list[CriminalRecord]:
        pass
