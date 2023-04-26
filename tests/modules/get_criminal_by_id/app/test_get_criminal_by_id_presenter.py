from src.modules.get_criminal_by_id.app.get_criminal_by_id_presenter import get_criminal_by_id_presenter


class TesteGetCriminalByIdPresenter:
    def test_get_criminal_by_id_presenter(self):
        event ={
            "body" : {
                "record_id" : "oiue281u"
            }
        }

        response = get_criminal_by_id_presenter(event, None)

        expect = {
            "criminal":{
                "criminal_id": "oiue281u",
                "name": "Coringa",
                "description":"palhaco",
                "gender":"NON_BINARY",
                "favorite_region":"WAYNE_TOWER",
                "powers":"risadinha",
                "crime":{
                    "id": "124",
                    "type_crime":"DOMESTIC_VIOLENCE"
                }
            },
            "message": "the criminal was retrieved successfully"
        }

        assert response.status_code == 200
        assert response.body == expect
