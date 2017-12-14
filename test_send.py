import numpy as np
import json
import tensorflow as tf
import base64
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from PIL import Image
from flask import Flask, request, jsonify
from get_prediction import get_prediction

app = Flask(__name__)

@app.route('/test_send', methods=['POST'])
def image_send():
    j_dict = request.json
    """    try:
        j_dict = json.dumps(j_dict)
        j_dict = json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)
    """
    # decode the base64 string into bytes
    image_b64_data = j_dict['im64']
    buf = io.BytesIO(image_b64_data)

    #save bytes to temp.jpg on disk
    filename = "temp.jpg"
    with open(filename, "wb") as image_out:
        image_out.write(base64.b64decode(buf))

    #read in temp.jpg using matplotlib.image's imread to give us the correct numpy.ndarray to pass into get_prediction
    image = mpimg.imread(temp.jpg)

    (label, prediction) = get_prediction(image)

    label_dict = {"diagnosis": label.tolist()}
    probability_dict = {"likelihood": prediction.tolist()}
    results_content = jsonify([label_dict], [probability_dict])

    print(results_content)

    return results_content
