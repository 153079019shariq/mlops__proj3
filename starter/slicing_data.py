
import os
import pandas as pd
import pickle
from starter.ml.data import process_data
from starter.ml.model import train_model,inference,compute_model_metrics
from sklearn.model_selection import train_test_split


def data_slice():
  
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
  
  df = pd.read_csv("data/census.csv")
  _, test = train_test_split(df, test_size=0.20)
  model = pickle.load(open( os.path.join("model",'trainedmodel.pkl'), 'rb'))
  lb  = pickle.load(open( os.path.join("model",'label_bin.pkl'), 'rb'))
  encoder = pickle.load(open( os.path.join("model",'encoder.pkl'), 'rb'))
   

  with open(os.path.join("slice_data","slice_data.txt"),"w") as f:
    for feature in cat_features:
      for val in test[feature].unique():
        df_temp = test.loc[test[feature]==val,:]
        X_test, y_test, encoder_test, lb_test = process_data(df_temp, categorical_features=cat_features, label="salary", training=False,encoder = encoder, lb=lb)
        y_pred = inference(model,X_test)
        precision,recall,fbeta = compute_model_metrics(y_test,y_pred)
        stri = f"Feature {feature} is having value {val}" +", precision  {:.2f}".format(precision) + ", recall {:.2f}".format(recall) +", fbeta {:.2f}".format(fbeta)
        print(stri) 
        f.write(stri)
        f.write("\n")
   
if __name__ =="__main__":
  data_slice()
  














