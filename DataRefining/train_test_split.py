# importing Statements
import pandas as pd
from sklearn.model_selection import train_test_split


def split_data():
    
    # reading dataset
    asd_data = pd.read_csv('./Datasets/clean_toddlers_data.csv', index_col=0)

    # Defining variable with independent features
    X = asd_data.drop('Class', axis=1)

    # Defining variable with dependent features
    Y = asd_data['Class']

    # Creating train & test sets
    # Training Data = 80% of the total Dataset
    # Test Data = 20% of the total Dataset
    X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.20, random_state=101)

    return X_train, Y_train, X_test, Y_test

# import these variables to Models
# X --> independent variable
# Y --> Dependent variable

# model <- X_train , y_train

# model <- X_test  output : Y_predicted 
# compare Y_predicted with Y_test

# 3 diff files --> 3 models
# 1 python file for Flask API
# 1 python file for database connection
