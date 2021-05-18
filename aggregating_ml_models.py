# importing statements
import sys
import pandas as pd


def get_models_result(patient_df):
    result= {}
   
    try:
        sys.path.append('P:\FY_Project\ADABoost')
        from ada_boost import ADA_Boost_Model
        result_ada = ADA_Boost_Model(patient_df)
        result['ada'] = result_ada
    
    except Exception as ex:
        print('Exception raised in ADABoost Algorithm',ex)


    try:
        sys.path.append('P:\FY_Project\KnnClassifier')
        from KNN import KNN_Model
        result_knn = KNN_Model(patient_df)
        result['knn'] = result_knn
        
    except Exception as ex:
        print('Exception raised in KNN algorithm',ex)

    
    try:
        sys.path.append('P:\FY_Project\LogisticRegression')
        from logistic_reg_model import Logistic_Regression_Model
        result_lr = Logistic_Regression_Model(patient_df)
        result['lr']= result_lr
        
    except Exception as ex:
        print('Exception raised in Logistic regression algorith',ex)



    
    try:
        sys.path.append('P:\FY_Project\RandomForest')
        from random_forest_model import Random_Forest_Model

        result_rf = Random_Forest_Model(patient_df)
        result['rf'] = result_rf
        
    except Exception as ex:
        print('Exception raised in Random Forest algorithm',ex)



    
    try:
        sys.path.append('P:\FY_Project\SVMClassifier')
        from SVC import SVC_Model
        result_svm = SVC_Model(patient_df)
        result['svc'] = result_svm

    except Exception as ex:
        print('Exception raised in KNN algorithm method',ex)

    return result


def refine_result_data(patient_data):
    refined_result_dict = {}
    result_dict = get_models_result(patient_data)
    
    
    for models in result_dict:
        for i in result_dict[models]:
            if i =='classification_report' or i == 'confusion_matrix':
                continue

            elif i == 'predction_of_test_data':
                refined_result_dict [ models + '_' + i ] = str(result_dict [models] [i][0])
            else:
                refined_result_dict [ models +'_'+ i ] = str(result_dict [models] [i])
                

    return refined_result_dict

## For testing
# lis_col = [ 'A1', 'A2', 'A3','A4','A5','A6','A7','A8','A9','A10','Age_Mons','Sex','Ethnicity','Jaundice','Family_mem_with_ASD']

# # defining values of columns
# var = [1,1,0,0,0,1,1,0,0,0,24,0,2,1,0]
# df = pd.DataFrame(var).transpose()
# df.columns = lis_col

# print(refine_result_data(df))


# print(get_models_result())