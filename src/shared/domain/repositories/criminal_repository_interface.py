from abc import ABC, abstractmethod
from src.shared.domain.entities.criminal_entity import Criminal

class ICriminalRepository(ABC):

    @abstractmethod
    def create_criminal(self) -> Criminal:
        pass

    @abstractmethod
    def get_criminal_by_id(self, id:str) -> Criminal:
        pass
