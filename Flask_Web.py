import numpy as np
import json
import tensorflow as tf
import base64
import io
#from pymodm import connect
#from pymodm import MongoModel, fields
from get_prediction import get_prediction
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image 

patient_counter = 0

# connect("mongodb://vcm-1856.vm.duke.edu:5900/melanoma_db")
app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/api/*":{"origins": "*"}})

# class User(MongoModel):
#     patient_id = fields.Integer()
#     p_malignant = fields.FloatField()
#     p_benign = fields.FloatField()
#     malignant_flag = fields.Integer() ....flag ==1 if p_mal > p_ben


@app.route("/WebAppMelanomaData", methods=['POST'])
def melanoma_results():
    """
        Accepts JSON dictionaries from Web Client for decoding the base64 data format to
        image data, processing the image with the get_prediction model, and returning results
        to the web client on port 5900
        :param: base64 data format in JSON dictionary
        :param: jpg image file for upload (input)
        :param: Flask App: WebAppMelanomaData
        :param: Port 5900
        :rtype: Diagnosis of malignancy in melanoma
    """
    # initialize array for image data, convert back from base64

    j_dict = request.json

    try:
        j_dict = json.dumps(j_dict)
        j_dict = json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)

    image_b64_data = j_dict['image']
    data = image_b64_data[0]
    msg = base64.b64decode(data)
    buf = io.BytesIO(msg)
    im_data = np.array(Image.open(buf))
    (labels, predictions) = get_prediction(im_data)
    label_dict = {"labels": labels}
    prediction_dict = {"prediction": np.float64(predictions).tolist()}
    results_content = jsonify([label_dict, prediction_dict])

    print(results_content)

    return results_content


"""
    c = 0
    results_content = {}
    for x in range(0, len(j_dict)):
        # decode base64 back to image
        data_key = "image" + str(c)
        data = j_dict[data_key]
        msg = base64.b64decode(data)
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

"""

if __name__ == "__main__":
    app.run(port=5900, host="0.0.0.0")
