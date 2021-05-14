# Logistic regression is a supervised learning classification algorithm used to predict the probability of a target variable.

# importing Libraries
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import sys
import pandas as pd


# Getting Splitted Datasets 
try:
    sys.path.append('P:\FY_Project\DataRefining')
    from train_test_split import split_data
    X_train, Y_train, X_test, Y_test = split_data()

except Exception as e:
    print("Exception caught in reading datasets",e)


def Logistic_Regression_Model( testing_data ):
    try:
        # Creating LR Model 
        logistic_reg_model = LogisticRegression(max_iter=200)

        # Training the Model
        logistic_reg_model.fit(X_train,Y_train)

        # Predicting values for class_label
        y_predicted =   logistic_reg_model.predict(X_test)

        # Calculating Model reports
        dict_report = {}
        dict_report ['accuracy_score'] = accuracy_score( y_true = Y_test, y_pred = y_predicted ) 
        dict_report ['classification_report'] = classification_report( Y_test, y_predicted )
        dict_report ['confusion_matrix'] = confusion_matrix( Y_test, y_predicted )
        dict_report ['predction_of_test_data'] = logistic_reg_model.predict(testing_data)
        
        return dict_report


    except Exception as ex:
        print('Caught Excption in model training / Prediction ',ex)








# For Testing
## Evaluating Model

# defining columns
lis_col = [ 'A1', 'A2', 'A3','A4','A5','A6','A7','A8','A9','A10','Age_Mons','Qchat-10-Score','Sex','Ethnicity','Jaundice','Family_mem_with_ASD']

# defining values of columns
var = [1,1,0,0,0,1,1,0,0,0,24,4,0,2,1,0]
df = pd.DataFrame(var).transpose()
df.columns = lis_col

# predicting dependant variable
result = Logistic_Regression_Model(df)

for i in result:
    print( i,result[i])

# Results will be same for all program execution because Ramdom state in train_test_split.py is constant 

# https://stackoverflow.com/questions/62658215/convergencewarning-lbfgs-failed-to-converge-status-1-stop-total-no-of-iter ( Why we took Max_itr= 200)
