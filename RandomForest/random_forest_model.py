# importing Libraries
from sklearn.ensemble import RandomForestClassifier
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

def Random_Forest_Model( testing_data):
    try:
        # Creating RF Model 
        random_forest_model = RandomForestClassifier(n_estimators=50)

        # Training the Model
        random_forest_model.fit(X_train,Y_train)

        # Predicting values for class_label
        y_predicted =   random_forest_model.predict(X_test)

        # Calculating Model reports
        dict_report = {}
        dict_report [ 'model' ] = 'Random Forest'
        dict_report ['test_accuracy_score'] = accuracy_score( y_true = Y_test, y_pred = y_predicted ) 
        dict_report ['train_accuracy_score'] = accuracy_score(Y_train, random_forest_model.predict(X_train)) 
        dict_report ['classification_report'] = classification_report( Y_test, y_predicted )
        dict_report ['confusion_matrix'] = confusion_matrix( Y_test, y_predicted )
        dict_report ['predction_of_test_data'] = random_forest_model.predict(testing_data)
        
        return dict_report


    except Exception as ex:
        print('Caught Excption in model training / Prediction ',ex)


# # For Testing
# ## Evaluating Model

# # defining columns
# lis_col = [ 'A1', 'A2', 'A3','A4','A5','A6','A7','A8','A9','A10','Age_Mons','Sex','Ethnicity','Jaundice','Family_mem_with_ASD']

# # defining values of columns
# var = [1,1,0,0,0,1,1,0,0,0,24,0,2,1,0]
# df = pd.DataFrame(var).transpose()
# df.columns = lis_col

# # predicting dependant variable
# result = Random_Forest_Model(df)

# for i in result:
#     print( i,result[i])
# Results will be same for all program execution because Ramdom state in train_test_split.py is constant 