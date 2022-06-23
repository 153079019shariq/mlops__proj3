import pytest
import pickle
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
@pytest.fixture(scope="session")
def data():
  df = pd.read_csv("data/census.csv")
  return df



def test_data_shape(data):
 # Check he shape of the data
 assert data.shape[0]>10000
 assert data.shape[1]==15


def test_no_of_categorical(data):
 # Check the numbber o categorical variable
 count = 0
 for col_name in data.columns:
   if(data[col_name].nunique()<=20):
     count +=1
 assert count -1 ==8  # -1 due to target being categroical


def test_percentage_missing(data):
  percent = data.isnull().sum()/data.count()*100
  percent =percent.reset_index()
  percent.columns = ["col_name","percent_missing"]
  for i in range(len(percent)):
    assert percent.loc[i,"percent_missing"]<10



def test_model():

    """ Model should be Logistic Regression as it was used for training """
    
    model = pickle.load(open( os.path.join(os.getcwd(),"model",'trainedmodel.pkl'), 'rb'))
    assert isinstance(model,LogisticRegression) 


"""
val = data()
test_model()
test_data_shape(val)
test_percentage_missing(val)
test_no_of_categorical(val)
"""
