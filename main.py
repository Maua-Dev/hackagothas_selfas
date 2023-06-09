from fastapi import FastAPI
from src.modules.create_criminal_record.app.create_criminal_record_presenter import create_criminal_record_presenter
from src.modules.delete_criminal_record.app.delete_criminal_record_presenter import delete_criminal_record_presenter
from src.modules.get_all_criminal_records.app.get_all_criminal_records_presenter import get_all_criminal_records_presenter
from src.modules.get_criminal_by_id.app.get_criminal_by_id_presenter import get_criminal_by_id_presenter
from src.modules.get_criminal_record_by_id.get_criminal_record_by_id_presenter import \
    get_criminal_record_by_id_presenter
from src.modules.update_criminal_record.app.update_criminal_record_presenter import update_criminal_record_presenter

app = FastAPI()

@app.post("/create_criminal_record/")
def create_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    response = create_criminal_record_presenter(event, None)
    return response

@app.post("/update_criminal_record")
def create_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    response = update_criminal_record_presenter(event, None)
    return response

@app.get("/get_criminal_record_by_id/")
def get_criminal_record_by_id(record_id = None):
    event = {
        "body":{},
        "headers": {},
        "query_params": {
            "criminal_record_id": record_id
        }
    }
    response = get_criminal_record_by_id_presenter(event, None)
    return response


@app.post("/delete_criminal_record")
def create_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    response = delete_criminal_record_presenter(event, None)
    return response

@app.get("/get_all_criminal_records/")
def get_all_criminal_records():
    event = {
        "body": {}
    }
    response = get_all_criminal_records_presenter(event, None)
    return response

@app.get("/get_criminal_by_id/")
def get_criminal_by_id(record_id = None):
    event = {
        "body":{},
        "headers": {},
        "query_params": {
            "record_id": record_id
        }
    }
    response = get_criminal_by_id_presenter(event, None)
    return response
