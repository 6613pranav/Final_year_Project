from flask import Flask, render_template, request, jsonify

try:
    # importing refine_result_data method from aggregating_ml_models module
    from aggregating_ml_models import refine_result_data

    # importing reframe_test_data method from converting_json_to_df module
    from converting_json_to_df import reframe_test_data

    # importing data_for_html_page method from get_data_for_result_page module
    from get_data_for_result_page import data_for_html_page

    # importing send_email_to_patient method from SendEmail module
    from SendEmail import send_email_to_patient

except Exception as ex:
    print("Exception raised in reading aggregating ml models.py",ex)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('questionaire.html')

@app.route('/ques', methods=["POST"])
def get_values():
    global final_result_dict
    dict_res={}
    dict_res['ques1'] = request.form.get("question1")
    dict_res['ques2'] = request.form.get("question2")
    dict_res['ques3'] = request.form.get("question3")
    dict_res['ques4'] = request.form.get("question4")
    dict_res['ques5'] = request.form.get("question5")
    dict_res['ques6'] = request.form.get("question6")
    dict_res['ques7'] = request.form.get("question7")
    dict_res['ques8'] = request.form.get("question8")
    dict_res['ques9'] = request.form.get("question9")
    dict_res['ques10'] = request.form.get("question10")
    dict_res['Age_Mons'] = request.form.get("bdate")
    dict_res['sex'] = request.form.get("gender")
    dict_res['ethinicity'] = request.form.get("origin")
    dict_res['jaundice'] = request.form.get("jaundice")
    dict_res['family_member_with_ASD'] = request.form.get("fasd")
    dict_res['name'] = request.form.get("fname") + " "  + request.form.get("lname")
    dict_res['who_completed_the_test'] = request.form.get("who_completed_the_test")
    dict_res['email'] = request.form.get("email")

    try:
        # this method converts dict response from frontend to dataframe
        patient_test_dataframe = reframe_test_data(dict_res)
        print('Converted from front end to dataframe --> api.py')
       
        # 'refine_result_data' method calculates results from different ML models and returns a dict
        ml_result_dict = refine_result_data(patient_test_dataframe)
        print('Got results from ML algos --> api.py')
       
        
        # combiming data for the 'result_page.html'
        final_result_dict = data_for_html_page( dict_res, ml_result_dict)
        print("Combined data from two dicts --api.py")

        # send email to user
        email_status = send_email_to_patient(final_result_dict)
        print("email sent successfully")

        final_result_dict['email'] = final_result_dict ['email'] + "  (" + email_status + ")"

        return render_template ('result_page.html', result= final_result_dict)

        

    except Exception as e:
        print("Exception caught in converting data ", e)
        return '<h1 style="background:red;"> An Error Occured in API.py <br> Exception = {}</h1>'.format(e)

@app.route('/admin')
def admin_result():
    try:
        return render_template ('results.html',result=final_result_dict)
    
    except Exception as e:
        print("Exception caught in converting data ", e)
        return '<h1 style="background:red;"> An Error Occured in API.py <br> Exception = {}</h1>'.format(e)
    

    





app.run(debug=True,port=2098)
# host='0.0.0.0', port=81