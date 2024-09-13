from flask import Flask, render_template, request
import numpy as np
import joblib
import pickle
import os
#import sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

def predictor(feature_list):
    to_predict = np.array(feature_list).reshape(1, -1)
    model_path = os.path.abspath(r"C:\Users\sastr\Intrusion Detection\xgboost_best_model.pkl")
    loaded_model = joblib.load(model_path)
    result = loaded_model.predict(to_predict)
    if result[0]==0:
        return "Beningn Traffic"
    elif result[0]==1:
        return "Attack type - DoS"
    elif result[0]==2:
        return "Attack type - Probe"
    elif result[0]==3:
        return "Attack type - R2L"
    elif result[0]==4:
        return "Attack type - U2R"

    

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form['features']
        to_predict_list = list(map(float, to_predict_list.split(',')))  # Split and convert to float
        result = predictor(to_predict_list)
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)