#contains accuracy, precision, recall, f1 score and confusion matrix for classification problems and MAE, MSE and RMSE for regression problems
"""
#accuracy means the ratio of correctly predicted observations to the total observations
#accuracy=correct predictions/total predictions let total prediction be 100 and correct prediction be 90 then accuracy will be 90/100=0.90 or 90%
#accuracy = (TP+TN)/(TP+TN+FP+FN) where TP is true positive, TN is true negative, FP is false positive and FN is false negative

#precision is the ratio of correctly predicted positive observations to the total predicted positive observations
#precision=correctly predicted positive observations/total predicted positive observations let total predicted positive be 100 and correctly predicted positive be 80 then precision will be 80/100=0.80 or 80%
#precision=TP/(TP+FP) where TP is true positive and FP is false positive

#recall is the ratio of correctly predicted positive observations to the all observations in actual class
#recall=correctly predicted positive observations/total actual positive observations for example if total actual positive is 100 and correctly predicted positive is 80 then recall will be 80/100=0.80 or 80%
#recall=TP/(TP+FN) where TP is true positive and FN is false negative

#f1 score is the weighted average of precision and recall it is used when we need to seek a balance between precision and recall and there is an uneven class distribution
#f1 score=2*(precision*recall)/(precision+recall) for example if precision is 0.80 and recall is 0.80 then f1 score will be 2*(0.80*0.80)/(0.80+0.80)=0.80 or 80%
"""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
def evaluate_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }
y_true = [ 1, 0, 1, 1, 0, 1, 1] #true labels
y_pred = [ 1, 0, 1, 0, 0, 1, 1]   #predicted labels
results = evaluate_model(y_true, y_pred)
print("Model Evaluation Results:")
print(f"Accuracy: {results['accuracy']:.2f}")   
print(f"Precision: {results['precision']:.2f}")   
print(f"Recall: {results['recall']:.2f}")   
print(f"F1 Score: {results['f1_score']:.2f}")  





"""
#confusion matrix is a table that is used to evaluate the performance of a classification model it shows the true positive, true negative, false positive and false negative values
#TP=> actual=true and predicted=true
#TN=> actual=false and predicted=false  
#FP=> actual=false and predicted=true
#FN=> actual=true and predicted=false
#    TP  FP
#    FN  TN
"""

from sklearn.metrics import confusion_matrix
def compute_confusion_matrix(y_true, y_pred):   
    cm = confusion_matrix(y_true, y_pred)
    return cm

cm = compute_confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)






"""
#MAE (Mean Absolute Error) is the average of the absolute differences between the predicted values and the actual values it is used for regression problems
#MAE= (1/n) * Σ|y_true - y_pred| where n is the number of observations, y_true is the actual value and y_pred is the predicted value

#MSE (Mean Squared Error) is the average of the squared differences between the predicted values and the actual values it is also used for regression problems
#MSE= (1/n) * Σ(y_true - y_pred)^2 where n is the number of observations, y_true is the actual value and y_pred is the predicted value

#RMSE (Root Mean Squared Error) is the square root of the average of the squared differences between the predicted values and the actual values it is also used for regression problems
#RMSE= sqrt((1/n) * Σ(y_true - y_pred)^2)
"""

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
def evaluate_regression_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    
    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse
    }   
y_true = [3.5, 2.0, 4.0, 5.0] #true values
y_pred = [3.0, 2.5, 4.5, 5.0] #predicted values
regression_results = evaluate_regression_model(y_true, y_pred)      
print("Regression Model Evaluation Results:")
print(f"MAE: {regression_results['MAE']:.2f}")
print(f"MSE: {regression_results['MSE']:.2f}")
print(f"RMSE: {regression_results['RMSE']:.2f}")




