from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase

class Test_CreateCriminalRecordUsecase:
    
    def test_create_criminal_record_usecase(self):
        
        repo = CriminalRecordRepositoryMock()

        createUsecase = CreateCriminalRecordUsecase(repo)

        length_before = len(repo.criminal_records_list)


        criminal_record = CriminalRecord(id="jdiashq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
                                         is_in_jail=False, danger_score=94, criminal=repo.criminals_list[0])


        createUsecase(criminal_record) #Adicionando ficha no banco de dados

        criminal_record_response = repo.criminal_records_list[-1]

        length_after = len(repo.criminal_records_list)

        assert length_after == length_before + 1 #Vendo se a quantidade de fichas no banco aumento de vdd
        
        assert criminal_record_response == criminal_record #Vendo se o ultimo item adicionado é o item esperado

    # def test_create_criminal_record_usecase_criminal_record_id_already_exists(self):
    #     repo = CriminalRecordRepositoryMock()
    #
    #     usecase = CreateCriminalRecordUsecase(repo)
    #
    #     usecase()
    #
    #     criminal_record = CriminalRecord(id="jdiqhihq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
    #                        is_in_jail=False, danger_score=94, criminal=repo.criminals[0])
    #
    #
