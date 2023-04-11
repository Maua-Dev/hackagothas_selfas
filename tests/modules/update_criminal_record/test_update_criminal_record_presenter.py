import json

from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter
from src.shared.helpers.external_interfaces.http_models import HttpResponse


class Test_UpdateCriminalRecordPresenter:
    def test_update_record_presenter(self):
        event = {
            "body": {
                "record_id_to_update": "jdiqhihq",
                "type_crime": "NAZI",
                "is_in_jail": True,
                "danger_score": "13",
                "criminal_name": "Shaco",
                "criminal_id": "80",
                "criminal_description": "Um palhaco muito louco",
                "criminal_gender": "MALE",
                "criminal_favorite_region": "WAYNE_TOWER",
                "criminal_powers": "Boa oratoria"
            }
        }

        response = update_criminal_record_presenter(event, None)

        expect = {
            'criminal_record': {
                'record_id': 'jdiqhihq',
                'type_crime': 'NAZI',
                'is_in_jail': True,
                'danger_score': 13,
                'criminal': {
                    'name': 'Shaco',
                    'id': '80',
                    'description': 'Um palhaco muito louco',
                    'gender': 'MALE',
                    'favorite_region': 'WAYNE_TOWER',
                    'power': 'Boa oratoria'
                }
            },
            "message": "the criminal record was updated successfully"
        }

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expect

    def test_update_criminal_record_with_id_that_doesnt_exist(self):
        event = {
            "body": {
                "record_id_to_update": "Um id que não existe",
                "type_crime": "NAZI",
                "is_in_jail": True,
                "danger_score": "13",
                "criminal_name": "Shaco",
                "criminal_id": "80",
                "criminal_description": "Um palhaco muito louco",
                "criminal_gender": "MALE",
                "criminal_favorite_region": "WAYNE_TOWER",
                "criminal_powers": "Boa oratoria"
            }
        }

        response = update_criminal_record_presenter(event, None)

        expect = HttpResponse(
            status_code=404,
            body="No items found for Criminal Record ID",
            headers={})

        assert response["status_code"] == 404
        assert json.loads(response["body"]) == expect.body