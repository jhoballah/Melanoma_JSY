import numpy as np
import json
import tensorflow as tf
import base64
from pymodm import connect
from pymodm import MongoModel, fields
#suyash's code:
from bme590_melanoma_detection.get_prediction import get_prediction

patient_counter = 0

from flask import Flask, request, jsonify
#connect("mongodb://vcm-1856.vm.duke.edu:5900/melanoma_db")
app = Flask(__name__)


# class User(MongoModel):
#     patient_id = fields.Integer()
#     p_malignant = fields.FloatField()
#     p_benign = fields.FloatField()
#     malignant_flag = fields.Integer() ....flag ==1 if p_mal > p_ben

@app.route("/CloudMelanomaData", methods=['POST'])
def melanoma_results():
    """
    #sphinx
    """
    # initialize array for image data, convert back from base64

    j_dict = request.json

    try:
        j_dict = json.dumps(j_dict)
        j_dict = json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)

    image_b64_data = np.array(j_dict['im64'])

    img = base64.b64decode(image_b64_data)

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


