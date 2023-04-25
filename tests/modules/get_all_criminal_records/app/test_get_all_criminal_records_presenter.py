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
                    'is_in_jail':False,
                    'danger_score':94,
                    'criminal':{
                       'name':'Coringa',
                       'id':'oiue281u',
                       'description':'palhaco',
                       'gender':'NON_BINARY',
                       'favorite_region':'WAYNE_TOWER',
                       'power':'risadinha',
                       'crimes_list':'[]'
                    }
                },
                'message':'Criminal record was created'
            },
            {
                'criminal_record':{
                    'record_id':'asadwa',
                    'is_in_jail':True,
                    'danger_score':27,
                    'criminal':{
                       'name':'Cersei',
                       'id':'vdajndkja',
                       'description':'filha da puta, vadia',
                       'gender':'FEMALE',
                       'favorite_region':'OLD_GOTHAM',
                       'power':'manipuladora'
                    }
                },
                'message':'Criminal record was created'
            }
        ]

        assert response["status_code"] == 200
        assert json.loads(response["body"]) == expect
