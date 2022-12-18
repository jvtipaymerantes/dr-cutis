from flask import render_template, jsonify, Flask, redirect, url_for, request
import random
import os
import numpy as np
from keras.applications.mobilenet import MobileNet 
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input, decode_predictions
from keras.models import model_from_json
from io import BytesIO
import keras
from keras import backend as K
import tensorflow as tf
import tempfile
import cv2


app = Flask(__name__)

SKIN_CLASSES = {
  0: 'Actinic Keratoses (Solar Keratoses) or intraepithelial Carcinoma (Bowen’s disease)',
  1: 'Basal Cell Carcinoma',
  2: 'Benign Keratosis',
  3: 'Dermatofibroma',
  4: 'Melanoma',
  5: 'Melanocytic Nevi',
  6: 'Vascular skin lesion'
}

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/templates/termscond.html')
def termscond():
    return render_template('termscond.html')

@app.route('/templates/form.html')
def form():
    return render_template('form.html')

@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        path='static/data/'+f.filename
        f.save(path)
        j_file = open('modelnew.json', 'r')
        loaded_json_model = j_file.read()
        j_file.close()
        model = model_from_json(loaded_json_model)
        model.load_weights('modelnew.h5')
        file_bytes = f.read()
        np_array = np.frombuffer(file_bytes, np.uint8)
        img1 = cv2.imread(path, cv2.IMREAD_COLOR)
        img1 = cv2.resize(img1, (224,224))
        img1 = img1.reshape((1,224,224,3))
        img1 = img1/255
        prediction = model.predict(img1)
        pred = np.argmax(prediction)
        disease = SKIN_CLASSES[pred]
        accuracy = prediction[0][pred]
        K.clear_session()
    else:
        print('The image must resized to 224x224')
    return render_template('uploaded.html', title='Success', predictions=disease, acc=accuracy*100, img_file=f.filename)

if __name__ == "__main__":
    app.run(debug=True)