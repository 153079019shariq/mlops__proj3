
import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_post():
    data = json.dumps({
                      "age" : 39,
                     "workclass"     : "State-gov",
                     "fnlgt" : 77516,
                     "education"     : "Bachelors",
                     "education-num" : 13,  
                     "marital-status": "Never-married",
                     "occupation"    : "Adm-clerical",
                     "relationship"  : "Not-in-family",
                     "race"          : "White",
                     "sex"           : "Male",
                     "capital-gain"  : 2174,
                     "capital-loss"  : 0,
                     "hours-per-week": 40,
                     "native-country": "United-States"   
    })


    r = client.post("/item", data=data)
    print("Display_result")
    print(r.json()["result"])
    #assert r.json()["path"] == 42
    #assert r.json()["query"] == 5
    #assert r.json()["body"] == {"value": 10}

test_post()
