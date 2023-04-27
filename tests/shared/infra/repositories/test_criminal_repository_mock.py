import pytest
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock

class TestCriminalRepositoryMock:
    def test_get_criminal_by_id(self):
        repo = CriminalRepositoryMock()

        id_to_search = repo.criminals_list[0].criminal_id

        response = repo.get_criminal_by_id(id_to_search)

        expected = repo.criminals_list[0]

        assert response == expected
    
    def test_get_criminal_by_id_without_id(self):
        with pytest.raises(NoItemsFound):
            repo = CriminalRepositoryMock()
            
            id_to_search = "nao_existe"
            
            response = repo.get_criminal_by_id(id_to_search)
