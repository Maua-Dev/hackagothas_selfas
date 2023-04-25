import pytest
from src.modules.get_criminal_by_id.app.get_criminal_by_id_usecase import GetCriminalByIdUsecase
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.criminal_repository_mock import CriminalRepositoryMock


class TestGetCriminalByIdUsecase:
    def test_get_criminal_by_id_usecase(self):
        repo = CriminalRepositoryMock()
        usecase = GetCriminalByIdUsecase(repo)
        response = usecase("oiue281u")
        expected = repo.criminals_list[0]

        assert response == expected

    def test_get_criminal_by_id_without_id_existent(self):
        with pytest.raises(NoItemsFound):
            repo = CriminalRepositoryMock()
            usecase = GetCriminalByIdUsecase(repo)
            response = usecase("id_inexistente")

