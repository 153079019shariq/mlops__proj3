# Put the code for your API here.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import os
import pandas as pd
import pickle
from starter.ml.data import process_data
from starter.ml.model import train_model,inference,compute_model_metrics

class Modelclass(BaseModel):
  age: int
  workclass      : Literal['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov','Self-emp-inc', 'Without-pay', 'Never-worked']  
  fnlgt : int
  education      : Literal['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
  education_num  : int
  marital_status : Literal['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-spouse-absent', 'Separated', 'Married-AF-spouse', 'Widowed']
  occupation     :Literal['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service', 'Sales', 'Craft-repair', 'Transport-moving', 'Farming-fishing', 'Machine-op-inspct', 'Tech-support', 'Protective-serv', 'Armed-Forces', 'Priv-house-serv']
  relationship   :Literal['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
  race           :Literal['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'] 
  sex            :Literal['Male', 'Female']
  capital_gain   : int
  capital_loss   : int
  hours_per_week : int
  native_country :Literal['United-States', 'Cuba', 'Jamaica', 'India', '?', 'Mexico', 'South', 'Puerto-Rico', 'Honduras', 'England', 'Canada', 'Germany', 'Iran', 'Philippines', 'Italy', 'Poland', 'Columbia', 'Cambodia', 'Thailand', 'Ecuador', 'Laos', 'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic', 'El-Salvador', 'France', 'Guatemala', 'China', 'Japan', 'Yugoslavia', 'Peru', 'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago', 'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary', 'Holand-Netherlands']



app = FastAPI()

model = pickle.load(open( os.path.join("model",'trainedmodel.pkl'), 'rb'))
lb  = pickle.load(open( os.path.join("model",'label_bin.pkl'), 'rb'))
encoder = pickle.load(open( os.path.join("model",'encoder.pkl'), 'rb'))
cat_features = [
      "workclass",
      "education",
      "marital-status",
      "occupation",
      "relationship",
      "race",
      "sex",
      "native-country",
  ]

@app.get("/")
async def intro():
  return "Welcome to FastAPI"


@app.post("/item")
async def predict(item:Modelclass):
  item = item.dict()
  df = pd.DataFrame( {
                     "age" : [item["age"]],
                     "workclass"     : [item["workclass"]],
                     "fnlgt" : [item["fnlgt"]],
                     "education"     :[item["education"]],
                     "education-num" :[item["education_num"]],  
                     "marital-status":[item["marital_status"]],
                     "occupation"    :[item["occupation"]],
                     "relationship"  :[item["relationship"]],
                     "race"          :[item["race"]],
                     "sex"           :[item["sex"]],
                     "capital-gain"  :[item["capital_gain"]],
                     "capital-loss"  :[item["capital_loss"]],
                     "hours-per-week":[item["hours_per_week"]],
                     "native-country":[item["native_country"]] 
                     }
                   )
  X_test, y_test, encoder_test, lb_test = process_data(df, categorical_features=cat_features, training=False,encoder = encoder, lb=lb)
  y_pred = inference(model,X_test)
  print("y_test",y_test)
  print("y_predict",y_pred)
  return {"result":1}











