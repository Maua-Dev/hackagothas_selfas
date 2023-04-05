from fastapi import FastAPI

from src.modules.create_criminal_record.app.create_criminal_record_presenter import create_criminal_record_presenter

app = FastAPI()


@app.post("/create_criminal_record/")
def get_criminal_record(data: dict = None):
    event = {
        "body": {
            k: str(v) for k, v in data.items()
        }
    }
    response = create_criminal_record_presenter(event, None)
    return response
