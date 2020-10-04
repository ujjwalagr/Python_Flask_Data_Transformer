import flask
import pandas as pd
import transformer as tf
from flask import request,jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/jsontocsv', methods=['POST'])
def json_to_CSV():
    x=request.json
    reqobj=tf.transform(x)
    return reqobj

app.run()