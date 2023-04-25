from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.domain.repositories.criminal_repository_interface import ICriminalRepository
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.helpers.errors.usecase_errors import NoItemsFound

class CriminalRepositoryMock(ICriminalRepository):
    criminals_list : list[Criminal]

    def __init__(self):
        self.criminals_list = [Criminal(name="Coringa", criminal_id="oiue281u", description="palhaco",
                                gender=GENDER.NON_BINARY, favorite_region=FAVORITE_REGION.WAYNE_TOWER, powers="risadinha",
                                crime=Crime("124", TYPE_CRIME.DOMESTIC_VIOLENCE))
                                ,
                                Criminal(name="Cersei", criminal_id="vdajndkja", description="filha da puta, vadia", gender=GENDER.FEMALE,
                                favorite_region=FAVORITE_REGION.OLD_GOTHAM, powers="manipuladora",
                                crime=Crime("1212", TYPE_CRIME.NAZI))
                            ]
        
    def get_criminal_list(self) -> list[Criminal]:
        return self.criminals_list

    def create_criminal(self) -> Criminal:
        return self.criminal
    
    def get_criminal_by_id(self, id: str) -> Criminal:
        for criminal in self.criminals_list:
            if (criminal.criminal_id == id):
                return criminal

        raise NoItemsFound("Criminal Record ID")
