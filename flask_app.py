# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 08:33:47 2023

@author: Arijit Raha
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
app=Flask(__name__)
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predicted Value is" + str(prediction)



if __name__=='__main__':
    app.run()   
    
""" http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1 """
""" The Predicted Value is[0] """
