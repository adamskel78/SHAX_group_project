from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

import numpy as np
import pandas as pd
import json
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pickle import dump
from pickle import load


from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# loaded_model = tf.keras.models.load_model('trained_factors.h5')
loaded_model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

# engine = create_engine('postgresql://postgres:123456Mxm@localhost/Final_Project')
engine = create_engine('postgres://lwmwibmlxnccxq:7c382373e3f1f5053320d604e3b8b07c4235df46b4bbcc2017701e9996ae11eb@ec2-3-208-50-226.compute-1.amazonaws.com:5432/d44ajo2omj7b6t')
Base = automap_base()
Base.prepare(engine, reflect=True)
Cardio = Base.classes.cardio_table
session = Session(engine)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Transfer JSON file into DF. Plug DF into Trained model. Make predictions
    data = pd.DataFrame(data, index=[0])
    # data = data[['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']]
    data = data[['age','height','weight','ap_hi','ap_lo','cholesterol']]
    scaler = load(open('scaler.pkl', 'rb'))
    data = scaler.transform(data)
    # loaded_model = tf.keras.models.load_model('trained_factors.h5')
    loaded_model = pickle.load(open('model.pkl', 'rb'))
    data = loaded_model.predict_proba(data)
    if data[:,1][0] < 0.33:   
        suggestion = "Probability of Getting Cardiovascular Disease is Low."
    elif data[:,1][0] > 0.66:
        suggestion = "Probability of Cardiovascular Disease is High. Please consider to be checked by a doctor."
    else:
        suggestion = "Probability of Cardiovascular Disease is Medium. Please pay attention to Cardiovascular Disease Symptoms."
        
    probObj = {
        "Probability": str(data[:,1][0].round(2)),
        "Suggestions": suggestion
    }
    return jsonify(probObj)

@app.route("/record/<id>")
def record(id):
    df = pd.read_sql(f'SELECT * FROM cardio WHERE id = {id}',engine)
    df["age"] = df["age"].astype(int)
    df["prob"] = df["prob"].round(2)
    return df.to_json(orient='records')

# @app.route("/record/ids")
# def records():
#     df = pd.read_sql(f'SELECT id FROM cardio',engine)
#     return jsonify(df["id"].to_list())

if __name__ == "__main__":
    app.run(debug=True, port=5001)