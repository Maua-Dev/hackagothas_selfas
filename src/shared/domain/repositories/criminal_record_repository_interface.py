from abc import ABC, abstractmethod
from src.shared.domain.entities.criminal_record_entity import CriminalRecord


class ICriminalRecordRepository(ABC):

    @abstractmethod
    def create_criminal_record(self, criminal_record: CriminalRecord) -> CriminalRecord:
        pass
