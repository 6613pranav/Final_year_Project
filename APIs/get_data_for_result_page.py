from datetime import datetime

# changing attributes
# middle eastern --> 1    
# White European --> 2   
# Hispanic       --> 3
# black          --> 4             
# asian          --> 5
# south asian    --> 6
# Native Indian  --> 7
# Others         --> 8
# Latino         --> 9
# mixed          --> 10
# Pacifica       --> 11

dict_ethinicity = {1:'Middle Eastern', 2:'White European', 3:'Hispanic', 4:'Black', 5:'Asian', 6:'South Asian', 7:'Native Indian', 8:'Others', 9:'Latino', 10:'Mixed', 11:'Pacifica'}

def data_for_html_page(patient_data_dict, ml_result_dict):
    
    prediction_percentage = ( float(ml_result_dict['ada_test_accuracy_score']) * int(ml_result_dict['ada_predction_of_test_data']) ) + ( float(ml_result_dict['knn_test_accuracy_score']) * int (ml_result_dict['knn_predction_of_test_data']) )  + ( float(ml_result_dict['lr_test_accuracy_score']) * int(ml_result_dict['lr_predction_of_test_data']) ) + ( float(ml_result_dict['rf_test_accuracy_score']) * int(ml_result_dict['rf_predction_of_test_data']) ) + ( float(ml_result_dict['svc_test_accuracy_score']) * int(ml_result_dict['svc_predction_of_test_data']) )
    prediction_percentage = (prediction_percentage/5) * 100
    ml_result_dict ['prediction_percentage'] = str(prediction_percentage)
    ml_result_dict ['name'] = patient_data_dict['name']
    ml_result_dict ['sex']  = 'Female'  if patient_data_dict['sex'] == 1 else "Male"
    ml_result_dict ['who_completed_the_test'] = patient_data_dict['who_completed_the_test']
    ml_result_dict ['email'] = patient_data_dict['email']
    ml_result_dict ['who_completed_the_test'] = patient_data_dict['who_completed_the_test']
    ml_result_dict ['ethinicity'] = dict_ethinicity[ int(patient_data_dict['ethinicity']) ]
    ml_result_dict ['age'] = str(patient_data_dict['Age_Mons'])

    return ml_result_dict
    