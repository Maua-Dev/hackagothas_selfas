from abc import ABC, abstractmethod
from src.shared.domain.entities.criminal_entity import Criminal

class ICriminalRepository(ABC):

    @abstractmethod
    def create_criminal(self) -> Criminal:
        pass
