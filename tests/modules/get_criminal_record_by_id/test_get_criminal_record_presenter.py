
from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_presenter import \
    get_criminal_record_by_id_presenter
from src.shared.helpers.external_interfaces.http_models import HttpResponse


class Test_GetCriminalRecordByIdPresenter:

    def test_get_criminal_record_presenter_should_be_sucessful(self):
        event = {
            "body": {
                "criminal_record_id": "jdiqhihq"
            }
        }

        response = get_criminal_record_by_id_presenter(event, None)

        expect = {
            "criminal_record": {
                "record_id": "jdiqhihq",
                "is_in_jail": False,
                "danger_score": 94,
                "criminal": {
                    'name': 'Coringa',
                    'id': 'oiue281u',
                    'description': 'palhaco',
                    'gender': 'NON_BINARY',
                    'favorite_region': 'WAYNE_TOWER',
                    'power': 'risadinha',
                    'crime':{
                      'id':'124',
                      'type_crime':'DOMESTIC_VIOLENCE'
                   }
                }
            },
            "message": "the criminal record was retrieved successfully"
        }

        assert response.status_code == 200
        assert response.body == expect

    def test_get_criminal_record_presenter_should_return_404(self):
        event = {
            "body": {
                "criminal_record_id": "um id que nao existe"
            }
        }

        response = get_criminal_record_by_id_presenter(event, None)

        expect = HttpResponse(
            status_code=404,
            body="No items found for Criminal Record ID",
            headers={})

        assert response.status_code == 404
        assert response.body == expect.body
