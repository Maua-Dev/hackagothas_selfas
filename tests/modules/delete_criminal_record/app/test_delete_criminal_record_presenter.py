import json
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
from src.shared.domain.enums.type_crime_enum import TYPE_CRIME
from src.shared.helpers.external_interfaces.http_models import HttpResponse

class TestDeleteCriminalRecordPresenter:
    def test_delete_criminal_record_presenter(self):
        event = {
            "body":{
                "criminal_record_id":"jdiqhihq"
            }
        }

        response = delete_criminal_record_presenter(event, None)

        expect = {
            "criminal_record":  {
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
            "message": "Criminal record was deleted successfully"
        }

        assert response.status_code == 200
        assert response.body == expect

    def test_get_criminal_record_presenter_should_return_404(self):
        event = {
            "body": {
                "criminal_record_id": "id_non_existe"
            }
        }

        response = delete_criminal_record_presenter(event, None)

        expect = HttpResponse(
            status_code=404,
            body="No items found for Criminal Record ID",
            headers={})

        assert response.status_code == 404
        assert response.body == expect.body
