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

# import these variables to Mocels
