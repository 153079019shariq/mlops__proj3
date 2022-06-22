import requests
import json 

data =  json.dumps({
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


r = requests.post("https://shariq-demo.herokuapp.com/item" ,data=data)
print(r.json()["result"])
print(f"Status_code is {r.status_code}")

