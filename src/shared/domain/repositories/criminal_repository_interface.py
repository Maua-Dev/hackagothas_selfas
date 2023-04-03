from abc import ABC, abstractmethod
from shared.domain.entities.criminal_entity import Criminal


class ICriminalRepository(ABC):

    @abstractmethod
    def create_criminal(self) -> Criminal:
        pass
