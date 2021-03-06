
import json
from fastapi.testclient import TestClient

from main import app
import requests

client = TestClient(app)

def test_get():

 r = client.get("/" )
 assert r.status_code == 200
 assert r.json() == "Welcome to FastAPI.The app will predict whether income is less than or greater than 50k"



def test_get_incorrect():
 r = client.get("/" )
 assert r.status_code == 200
 assert r.json() != "Welcome to FastAPI.Hello"


def test_post_negative():
    #Salary less than 50k
    data = json.dumps({
                     "age" : 39,
                     "workclass"     : "State-gov",
                     "fnlgt" : 77516,
                     "education"     : "Bachelors",
                     "education_num" : 13,  
                     "marital_status": "Never-married",
                     "occupation"    : "Adm-clerical",
                     "relationship"  : "Not-in-family",
                     "race"          : "White",
                     "sex"           : "Male",
                     "capital_gain"  : 2174,
                     "capital_loss"  : 0,
                     "hours_per_week": 40,
                     "native_country": "United-States"   
    })

    #r= requests.post("http://127.0.0.1:8000/item",data =data)
    r = client.post("/item", data=data)
    assert r.status_code == 200
    assert r.json() == { "result":['<=50K']}
    print(r.json())


def test_post_positive():
    #Salary greater than 50k
    data = json.dumps({
                     "age" : 47,
                     "workclass"     : "Self-emp-inc",
                     "fnlgt" : 181130,
                     "education"     : "Prof-school",
                     "education_num" : 15,  
                     "marital_status": "Married-civ-spouse",
                     "occupation"    : "Prof-specialty",
                     "relationship"  : "Husband",
                     "race"          : "White",
                     "sex"           : "Male",
                     "capital_gain"  :  99999,
                     "capital_loss"  : 0,
                     "hours_per_week": 50,
                     "native_country": "United-States"   
    })

    #r= requests.post("http://127.0.0.1:8000/item",data =data)
    r = client.post("/item", data=data)
    assert r.status_code == 200
    assert r.json() == { "result":['>50K']}
    print(r.json())



def test_post_failure_case1():
    #Passing random WRONG value for caegorical workclass  
    data = json.dumps({
                     "age" : 47,
                     "workclass"     : "Prof-school",
                     "fnlgt" : 181130,
                     "education"     : "Prof-school",
                     "education_num" : 15,  
                     "marital_status": "Married-civ-spouse",
                     "occupation"    : "Prof-specialty",
                     "relationship"  : "Husband",
                     "race"          : "White",
                     "sex"           : "Male",
                     "capital_gain"  :  99999,
                     "capital_loss"  : 0,
                     "hours_per_week": 50,
                     "native_country": "United-States"   
    })

    #r= requests.post("http://127.0.0.1:8000/item",data =data)
    r = client.post("/item", data=data)
    assert r.status_code != 200


def test_post_failure_case2():
    #Passing integer value for caegorical workclass which expects a string  
    data = json.dumps({
                     "age" : 47,
                     "workclass"     : 181130,
                     "fnlgt" : 181130,
                     "education"     : "Prof-school",
                     "education_num" : 15,  
                     "marital_status": "Married-civ-spouse",
                     "occupation"    : "Prof-specialty",
                     "relationship"  : "Husband",
                     "race"          : "White",
                     "sex"           : "Male",
                     "capital_gain"  :  99999,
                     "capital_loss"  : 0,
                     "hours_per_week": 50,
                     "native_country": "United-States"   
    })

    #r= requests.post("http://127.0.0.1:8000/item",data =data)
    r = client.post("/item", data=data)
    assert r.status_code != 200



test_get()
test_get_incorrect()
test_post_negative()
test_post_positive()
test_post_failure_case1()
test_post_failure_case2()
