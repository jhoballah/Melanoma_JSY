import numpy as np
import json
import base64
import io
#from pymodm import connect
#from pymodm import MongoModel, fields
from PIL import Image
import tensorflow as tf
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

    c = 0
    results_content = {}
    for x in range(0, len(j_dict)):
        # decode base64 back to image
        data_key = "image" + str(c)
        data = j_dict[data_key]
        print(data)
        msg = base64.b64decode(data[0])
        buf = io.BytesIO(msg)
        img = np.array(Image.open(buf))
        (labels, predictions) = get_prediction(img)
        prediction_key = "prediction" + str(c)
        # prediction_dict = {prediction_key: np.float64(predictions).tolist()}
        results_content[prediction_key] = np.float64(predictions).tolist()
        c = c + 1

    results_content = jsonify([results_content])
    return results_content

    # Populate MongoDB with results
    # if predictions[0]>predictions[1]:
    #   flag = 1
    #else:
    #   flag = 0
    # global patient_counter
    # patient_counter = patient_counter + 1
    # new_p = User(patient_id = patient_counter, p_malignant=predictions[0], p_benign=predictions[1],
    # malignant_flag = flag)
    # new_p.save()


if __name__=="__main__":
    app.run(port=5900, host="0.0.0.0")

