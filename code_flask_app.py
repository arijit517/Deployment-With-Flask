C:\Users\Arijit Raha\Desktop\Sample\DEPLOYMENT\FLASK

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
    variance=reqquest.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=reuest.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predicted Value is" + str(prediction)



if__name__=='__main__':
    app.run()