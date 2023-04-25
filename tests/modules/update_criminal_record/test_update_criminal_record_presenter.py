import json

from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter
from src.shared.helpers.external_interfaces.http_models import HttpResponse


class Test_UpdateCriminalRecordPresenter:
    def test_update_record_presenter(self):
        event = {
            "body": {
                "record_id_to_update": "jdiqhihq",
                "is_in_jail": True,
                "danger_score": 81,
                "criminal_name": "Charada",
                "criminal_id": "420",
                "criminal_description": "Umas charadas muito loucas",
                "criminal_gender": "MALE",
                "criminal_favorite_region": "WAYNE_TOWER",
                "criminal_powers": "Bela oratoria",
                "criminal_crimes_id": "32",
                "criminal_crimes_type": "MURDER"
            }
        }

        response = update_criminal_record_presenter(event, None)

        expect = {
            'criminal_record': {
                'record_id':'jdiqhihq',
                'is_in_jail':True,
                'danger_score':81,
                'criminal':{
                   'name':'Charada',
                   'id':'420',
                   'description':'Umas charadas muito loucas',
                   'gender':'MALE',
                   'favorite_region':'WAYNE_TOWER',
                   'power':'Bela oratoria',
                   'crime':{
                      'id':'32',
                      'type_crime':'MURDER'
                   }
                }
            },
            "message": "the criminal record was updated successfully"
        }

        assert response.status_code == 200
        assert response.body == expect

    def test_update_criminal_record_with_id_that_doesnt_exist(self):
        event = {
            "body": {
             "record_id_to_update": "um Id que nao existe",
                "is_in_jail": True,
                "danger_score": 81,
                "criminal_name": "Charada",
                "criminal_id": "420",
                "criminal_description": "Umas charadas muito loucas",
                "criminal_gender": "MALE",
                "criminal_favorite_region": "WAYNE_TOWER",
                "criminal_powers": "Bela oratoria",
                "criminal_crimes_id": "32",
                "criminal_crimes_type": "MURDER"
            }
        }

        response = update_criminal_record_presenter(event, None)

        expect = HttpResponse(
            status_code=404,
            body="No items found for Criminal Record ID",
            headers={})

        assert response.status_code == 404
        assert response.body == expect.body
