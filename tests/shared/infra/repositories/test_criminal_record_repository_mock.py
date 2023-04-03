from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Teste_CriminalRecordRepositoryMock:
    def teste_create_criminal_record(self):
        repo = CriminalRecordRepositoryMock()

        length_before = len(repo.criminal_records)

        repo.create_criminal_record(criminal_record=repo.criminal_records[0])

        length_after = len(repo.criminal_records)

        assert length_after == length_before + 1
