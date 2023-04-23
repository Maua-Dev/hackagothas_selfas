import json
from src.modules.get_all_criminal_records.app.get_all_criminal_records_presenter import get_all_criminal_records_presenter


class TestGetAllCriminalRecordsPresenter:
    def test_get_all_criminal_records_presenter(self):
        event = {}

        response = get_all_criminal_records_presenter(event, None)

        expect = [
            {
                'criminal_record':{
                    'record_id':'jdiqhihq',
                    'type_crime':'HATER_OF_INTERESTELLAR',
                    'is_in_jail':False,
                    'danger_score':94,
                    'criminal':{
                       'name':'Coringa',
                       'id':'oiue281u',
                       'description':'palhaco',
                       'gender':'NON_BINARY',
                       'favorite_region':'WAYNE_TOWER',
                       'power':'risadinha'
                    }
                },
                'message':'Criminal record was created'
            },
            {
                'criminal_record':{
                    'record_id':'223',
                    'type_crime':'HATER_OF_INTERESTELLAR',
                    'is_in_jail':True,
                    'danger_score':94,
                    'criminal':{
                       'name':'Coringa',
                       'id':'oiue281u',
                       'description':'palhaco',
                       'gender':'NON_BINARY',
                       'favorite_region':'WAYNE_TOWER',
                       'power':'risadinha'
                    }
                },
                'message':'Criminal record was created'
            }
        ]

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expect
