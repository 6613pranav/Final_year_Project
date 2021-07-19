from flask import Flask, render_template, request, jsonify
import sys


try:
    sys.path.append('P:\FY_Project')
    from aggregating_ml_models import refine_result_data

except Exception as ex:
    print("Exception raised in reading aggregating ml models.py",ex)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('questionaire.html')

@app.route('/ques', methods=["POST"])
def get_values():
    dict_res={}
    # name = request.form.get("gender")
    # print(name)
    # return "done"
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
    print(dict_res)

    try:
        sys.path.append('P:\FY_Project')
        from converting_json_to_df import reframe_test_data
        patient_test_dataframe = reframe_test_data(dict_res)
        result_dict = refine_result_data(patient_test_dataframe)
        print(result_dict)


    except Exception as e:
        print("Exception caught in converting data ", e)

    return render_template ('result.html', result=result_dict)





app.run(debug=True)
# host='0.0.0.0', port=81