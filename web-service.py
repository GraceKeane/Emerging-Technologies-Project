# Referances
# Adapted from - Flask; A Minimal Application;
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
import flask as fl
import numpy as np

app = fl.Flask(__name__)

@app.route('/uniform')
def uniform():
    return {'value': np.random.uniform()}

@app.route('/normal')
def normal():
    return{"value": np.random.normal()}