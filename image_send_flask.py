import numpy as np
import json
import tensorflow as tf
import base64
import io

from PIL import Image
from flask import Flask, request, jsonify
from get_prediction import get_prediction

app = Flask(__name__)


@app.route('/jawad', methods=['POST'])
def image_send():

    #should be image converted to base 64
    j_dict = request.json


    """    try:
        j_dict = json.dumps(j_dict)
        j_dict = json.loads(j_dict)
        # load is for file, loads is for string
    except ValueError:
        return send_error("Input is not JSON dictionary", 600)

    image_b64_data = j_dict['im64']

    print(j_dict)

    img = base64.b64decode(image_b64_data[0])


    filename="testfile.jpg"
    with open(filename, 'wb') as f:
        f.write(img)

    # return img

    """
    image_b64_data = j_dict['im64']

    # msg = msg[msg.find(b"<plain_txt_msg:img>") + len(b"<plain_txt_msg:img>"):
    # msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(image_b64_data[0])
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    # return img

    (label, prediction) = get_prediction(img)

    label_dict = {"diagnosis": label.tolist()}
    probability_dict = {"likelihood": prediction.tolist()} 
    results_content = jsonify([label_dict], [probability_dict])

    print(results_content)

    return results_content

if __name__=="__main__":
	app.run(port="5900",host="0.0.0.0")
