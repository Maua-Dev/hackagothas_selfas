from src.modules.get_all_criminal_records.app.get_all_criminal_records_usecase import GetAllCriminalRecordsUsecase
from src.modules.get_all_criminal_records.app.get_all_criminal_records_viewmodel import GetAllCriminalRecordsViewModel
from src.shared.domain.entities.crime_entity import Crime
from src.shared.domain.entities.criminal_entity import Criminal
from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.favorite_region_enum import FAVORITE_REGION
from src.shared.domain.enums.gender_enum import GENDER
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class TestGetAllCriminalRecordsViewModel:
    def test_get_all_criminal_records_viewmodel(self):
        criminal = Criminal("João Fraco (John Wick)", "69", "Doidão pq mataram o cachorro dele", GENDER.NON_BINARY, FAVORITE_REGION.AKRHAM_ASYLUM, "fica muito forte quando matam seu cachorro", Crime("42", TYPE_CRIME.MURDER))
        
        criminal_record = CriminalRecord("aaaa231", False, 99, criminal)

        criminal2 = Criminal("Konrad", "24", "chorão de mecg", GENDER.FEMALE, FAVORITE_REGION.OLD_GOTHAM, "fica forte pós provinha de mecg", Crime("27", TYPE_CRIME.CRIME_AGAINST_SELFAS_THE_BEST_PROJECT))
        
        criminal_record2 = CriminalRecord("2314adw3",  True, 2, criminal2)

        total_criminal_records: list[CriminalRecord] = [criminal_record, criminal_record2]

        view_model = GetAllCriminalRecordsViewModel(total_criminal_records)

        response: list = view_model.to_dict()

        assert type(response) == list
        assert len(response) == 2
        assert type(response[0]) == dict
        assert type(response[1]) == dict

        for index, value in enumerate(response):
            assert value["criminal_record"]["record_id"] == total_criminal_records[index].id
            assert value["criminal_record"]["is_in_jail"] == total_criminal_records[index].is_in_jail
            assert value["criminal_record"]["danger_score"] == total_criminal_records[index].danger_score
            assert value["criminal_record"]["criminal"] == total_criminal_records[index].criminal.to_dict()
            assert value["message"] == "Record was retrieved"

      