import numpy as np
import json
import tensorflow as tf
import base64
import io
from pymodm import connect
from pymodm import MongoModel, fields
from get_prediction import get_prediction
from flask import Flask, request, jsonify

patient_counter = 0

# connect("mongodb://vcm-1856.vm.duke.edu:5900/melanoma_db")
app = Flask(__name__)

# class User(MongoModel):
#     patient_id = fields.Integer()
#     p_malignant = fields.FloatField()
#     p_benign = fields.FloatField()
#     malignant_flag = fields.Integer() ....flag ==1 if p_mal > p_ben


@app.route("/CloudMelanomaData", methods=['POST'])
def melanoma_results():
    """
    sphinx
    """
    # initialize array for image data, convert back from base64

    j_dict = request.json

    try:
        j_dict = json.dumps(j_dict)
        j_dict = json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)

    # decode base64 back to image

    image_b64_data = j_dict['im64']
    msg = base64.b64decode(image_b64_data[0])
    buf = io.BytesIO(msg)
    img = np.array(Image.open(buf))

    # TensorFlow - Get_Prediction fxn

    (labels, predictions) = get_prediction(img)

    label_dict = {"diagnosis": labels.tolist()}
    probability_dict = {"likelihood": predictions.tolist()}

    results_content = jsonify([label_dict], [probability_dict])

    # if predictions[0]>predictions[1]:
    #   flag = 1
    #else:
    #   flag = 0
    # global patient_counter
    # patient_counter = patient_counter + 1
    # new_p = User(patient_id = patient_counter, p_malignant=predictions[0], p_benign=predictions[1],
    # malignant_flag = flag)
    # new_p.save()

    return results_content


