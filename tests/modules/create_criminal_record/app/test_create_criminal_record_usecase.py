from src.shared.domain.entities.criminal_record_entity import CriminalRecord
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock
from src.modules.create_criminal_record.app.create_criminal_record_usecase import CreateCriminalRecordUsecase

class Test_CreateCriminalRecordUsecase:
    
    def test_create_criminal_record_usecase(self):
        
        repo = CriminalRecordRepositoryMock()

        usecase = CreateCriminalRecordUsecase(repo)

        usecase(repo.criminal_records[0].danger_score, repo.criminal_records[0])

        criminal_record = CriminalRecord(id="jdiashq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
                           is_in_jail=False, danger_score=94, criminal=repo.criminals[0])
        
        length_before = len(repo.criminal_records)

        criminal_record_response = usecase(criminal_record=criminal_record)

        length_after = len(repo.criminal_records)

        assert length_after == length_before + 1
        
        assert criminal_record_response == criminal_record

    # def test_create_criminal_record_usecase_criminal_record_id_already_exists(self):
    #     repo = CriminalRecordRepositoryMock()

    #     usecase = CreateCriminalRecordUsecase(repo)

    #     usecase()

    #     criminal_record = CriminalRecord(id="jdiqhihq", type_crime=TYPE_CRIME.HATER_OF_INTERESTELLAR,
    #                        is_in_jail=False, danger_score=94, criminal=repo.criminals[0])
        
    #     with pytest
