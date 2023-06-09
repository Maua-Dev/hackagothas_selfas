import json

from src.modules.create_criminal_record.app.create_criminal_record_presenter import create_criminal_record_presenter


class Test_CreateRecordPresenter:
    def test_create_record_presenter(self):
        event = {
            "body": {
                "record_id": "42",
                "is_in_jail": True,
                "danger_score": 96,
                "criminal_name": "Charada",
                "criminal_id": "2",
                "criminal_description": "Umas charadas muito loucas",
                "criminal_gender": "MALE",
                "criminal_favorite_region": "WAYNE_TOWER",
                "criminal_powers": "Boa oratoria",
                "criminal_crimes_id": "20",
                "criminal_crimes_type":"MURDER"
            }
        }

        response = create_criminal_record_presenter(event, None)

        expect = {
            'criminal_record':{
                'record_id':'42',
                'is_in_jail':True,
                'danger_score':96,
                'criminal':{
                   'name':'Charada',
                   'id':'2',
                   'description':'Umas charadas muito loucas',
                   'gender':'MALE',
                   'favorite_region':'WAYNE_TOWER',
                   'power':'Boa oratoria',
                   'crime':{
                      'id':'20',
                      'type_crime':'MURDER'
                   }
                }
            },
            'message':'Criminal record was created'
        }

        assert response.status_code == 201
        assert response.body == expect
