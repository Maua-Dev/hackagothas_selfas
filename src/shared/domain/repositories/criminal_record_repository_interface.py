from abc import ABC, abstractmethod
from shared.domain.entities.criminal_record_entity import CriminalRecord
from shared.domain.entities.criminal_entity import Criminal


class ICriminalRepository(ABC):

    @abstractmethod
    def create_criminal_record(self, criminal: Criminal) -> CriminalRecord:
        pass
