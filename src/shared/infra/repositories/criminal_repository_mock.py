from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION


class CriminalRepositoryMock(ICriminalRepository):
    def __init__(self):
        self.criminal = Criminal(name="Coringa", criminal_id="oiue281u", description="palhaco",
                                 gender=GENDER.NON_BINARY, favorite_region=FAVORITE_REGION.WAYNE_TOWER, powers="risadinha")

    def create_criminal(self) -> Criminal:
        return self.criminal
