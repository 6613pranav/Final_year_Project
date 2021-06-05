# Importing Staements 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import sys  
import matplotlib.pyplot as plt


#Empty list for graph
results =[]

# Getting Splitted Datasets 
try:
    sys.path.append('P:\FY_Project\DataRefining')
    from train_test_split import split_data
    X_train, Y_train, X_test, Y_test = split_data()

except Exception as e:
    print("Exception caught in reading datasets",e)



try:

    # Calculating Accuracy of model with n_estimator value 1 to 200
    for k in range(1, 200):
        model = RandomForestClassifier(n_estimators=k)
        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)
        results.append(accuracy_score(Y_test, y_pred))


    # Plotting Graph
    plt.plot(range(1, 200), results)
    plt.xlabel('Value of n_estimators for Random Forest Classifier')
    plt.ylabel('Testing Accuracy')
    plt.savefig('./RandomForest/N_estimator_graph.png')

except Exception as ex:
    print("Caught Exception in training model", ex)

# Conclusion 
# from the graph we can observe that any value > 50 for N_estimator will give good results in terms of Accuracy