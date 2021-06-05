# importing Statements
import pandas as pd
import datetime as dt
from datetime import datetime

def reframe_test_data(dict):
    # defining columns of the test_sets
    total_cols_in_datasets = [ 'A1', 'A2', 'A3','A4','A5','A6','A7','A8','A9','A10','Age_Mons','Sex','Ethnicity','Jaundice','Family_mem_with_ASD']


    # counting the months
    today_date = datetime.today()
    date_of_birth = dict['Age_Mons'].split('-')
    num_months = (today_date.year - int(date_of_birth[0])) * 12 + (today_date.month - int(date_of_birth[1]))
    dict['Age_Mons'] = num_months


    # Label Encoding the testsets
    for i in dict:

        if dict[i] == 'yes' or dict[i] =='no':
            result = 1 if dict[i] == 'yes' else 0
            dict[i] = result
        
        elif i == 'sex':
            dict[i] = 0 if dict[i] == 'male' else 1
            
        else:
            continue




    patient_data = [ dict['ques1'], dict['ques2'], dict['ques3'], dict['ques4'], dict['ques5'], dict['ques6'], dict['ques7'], dict['ques8'], dict['ques9'], dict['ques10'], dict['Age_Mons'], dict['sex'], dict['ethinicity'],  dict['jaundice'], dict['family_member_with_ASD']]
    # var = [1,1,0,0,0,1,1,0,0,0,24,0,2,1,0]
    patient_data_df = pd.DataFrame( patient_data ).transpose()
    patient_data_df.columns = total_cols_in_datasets
    
    return patient_data_df




# # predicting dependant variable
# result = Random_Forest_Model(df)

# for i in result:
#     print( i,result[i])
# # Results will be same for all program execution because Ramdom state in train_test_split.py is constant 
# dict1 = {'ques1': 'no', 'ques2': 'no', 'ques3': 'no', 'ques4': 'yes', 'ques5': 'yes', 'ques6': 'yes', 'ques7': 'no', 'ques8': 'yes', 'ques9': 'yes', 'ques10': 'no', 'Age_Mons': '2021-01-22', 'sex': 'female', 'ethinicity': '7', 'jaundice': 'no', 'family_member_with_ASD': 'yes'}
# print(reframe_test_data(dict1))
