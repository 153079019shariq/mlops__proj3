# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
 The model used here is the Logistic regression

## Intended Use
  The model will predict whether the income is greater than or less than $50k

## Training Data
  80% of the data was used for the purpose of training

## Evaluation Data
  20% of the data was used for validation

## Metrics
 The metrics used for evaluating the model are precision,recall and f-beta
 The value obtained on the validation dataset are as follows:
   Precision : 0.706
   Recall    : 0.256
   F-beta    : 0.376

## Ethical Considerations
 The model should not be biased toward a gender or ethinic origin

## Caveats and Recommendations
  The performance of the model can be improved by hyperparameter tuning. Also tree based algorithm like XGBoost which gived better result could be tried out.

