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

engine = create_engine('postgresql://postgres:123456Mxm@localhost/Final_Project')
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
    probObj = {
        "Probability": str(data[:,1][0].round(2))
    }
    return jsonify(probObj)

@app.route("/demo")
def demo():
    results = session.query(Cardio.age).all()
    demo = list(np.ravel(results))
    session.close()
    return jsonify(demo)


if __name__ == "__main__":
    app.run(debug=True, port=5001)