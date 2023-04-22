from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.modules.get_all_criminal_records.app.get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewModel
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestGetAllCriminalRecordsViewModel:
    def test_get_all_criminal_records_viewmodel(self):
        criminal = Criminal("João Fraco (John Wick)", "69", "Doidão pq mataram o cachorro dele", GENDER.NON_BINARY, FAVORITE_REGION.AKRHAM_ASYLUM, "fica muito forte quando matam seu cachorro")
        
        criminal_record = CriminalRecord("aaaa231", TYPE_CRIME.FUCK_BOY, False, 99, criminal)

        criminal2 = Criminal("Konrad", "24", "chorão de mecg", GENDER.FEMALE, FAVORITE_REGION.OLD_GOTHAM, "fica forte pós provinha de mecg")
        
        criminal_record2 = CriminalRecord("2314adw3", TYPE_CRIME.CRIME_AGAINST_SELFAS_THE_BEST_PROJECT, True, 2, criminal2)

        total_criminal_records = [criminal_record, criminal_record2]

        view_model = GetAllCriminalRecordsViewModel(total_criminal_records)

        response = view_model.to_dict()

        assert type(response) == list
        assert len(response) == 2
        assert type(response[0]) == dict
        assert type(response[1]) == dict

        # for index,value in enumerate(response):
        #     assert value == total_criminal_records[index]

        # for value in response:
        #     assert value == total_criminal_records

      