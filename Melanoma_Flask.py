import numpy as np
import json
import tensorflow as tf
import base64
# suyash's code:
# import get_prediction as gp


from flask import Flask, request, jsonify
app = Flask(__name__)

#    pip install Flask
#    $ FLASK_APP = hello.py flask run

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

    return results_content


