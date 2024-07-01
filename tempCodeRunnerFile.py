import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os
print(os.getcwd())  # Print current working directory
print(os.listdir())  # Print a list of files in the current working directory

app=Flask(__name__)    
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)
