# Script to train machine learning model.
import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
from ml.data import process_data
from ml.model import train_model,inference,compute_model_metrics
# Add code to load in the data.
data = pd.read_csv("../data/census.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20,random_state=10)






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
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.
X_test, y_test, encoder_test, lb_test = process_data(
    test, categorical_features=cat_features, label="salary", training=False,
    encoder = encoder, lb=lb)


# Train and save a model.
model = train_model(X_train, y_train)



#Inference of the model
y_pred = inference(model,X_test)
#print(test.iloc[4,:])
#print(np.nonzero(y_pred))
#print(y_pred[4])

precision,recall,fbeta = compute_model_metrics(y_test,y_pred)

print(precision,recall,fbeta)

with open( os.path.join("../model",'trainedmodel.pkl'), 'wb') as files:
  pickle.dump(model, files)

with open( os.path.join("../model",'encoder.pkl'), 'wb') as files:
  pickle.dump(encoder, files)

with open( os.path.join("../model",'label_bin.pkl'), 'wb') as files:
  pickle.dump(lb, files)
