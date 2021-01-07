# Imports needed
import flask as fl
import numpy as np
import tensorflow as tf
from flask import request

# Create a new web app.
app = fl.Flask(__name__)

# Add root route. 
# Connects to style page (index.html)
@app.route("/")
def home():
  return app.send_static_file('index.html')

# Adapted from
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

@app.route("/power", methods=["POST"])
def powerOutput():
  ws = float(request.get_json()["value"])
  model = tf.keras.models.load_model("savedValues.h5")
  prediction = model.predict([ws])
  lp = prediction.tolist()
  return {'prediction': lp[0]}

if __name__ == '__main__':
  app.run(debug=True)