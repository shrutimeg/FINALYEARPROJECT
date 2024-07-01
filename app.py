import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle
import os
print(os.getcwd())  # Print current working directory
print(os.listdir())
app = Flask(__name__,template_folder='template')
model=pickle.load(open('tranning/CKD.pkl','rb'))
@app.route("/")
def Hello():
    return render_template('home.html')

@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')
@app.route('/aboutckd' ,methods=['POST','GET'])
def aboutckd():
    return render_template('aboutckd.html')
@app.route('/contact' ,methods=['POST','GET'])
def contact():
    return render_template('contact.html')
@app.route('/team' ,methods=['POST','GET'])
def team():
    return render_template('team.html')


@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features=[float(x) for x in request.form.values()]
    features_value=[np.array(input_features)]

    # features_name=['blood_urea','blood glucose random','coronary_artery_disease','anemia','pus_cell','red_blood_cells','diabetesmellitus','pedal_edema']
    features_name=['red_blood_cells','pus_cell','blood gulcose random','blood_urea','pedal_edema','anemia','diabetesmellitus','coronary_artery_disease']
    df=pd.DataFrame(features_value, columns=features_name)
    output=model.predict(df)
    return render_template('result.html',prediction_text=output)

app.run(debug=True)