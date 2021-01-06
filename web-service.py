# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

import tensorflow as tf

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return app.send_static_file('index.html')

@app.route("/powerVal", method=["POST"])
def powerValuesOutput():
  ws = float(request.get_json()["val"])
  projectModel = tf.keras.models.load_projectModel("savedValues.h5")
  pred = projectModel.predict([windspeed])
  listPred = prediction.tolist()
  return {'prediction': listPred[0]}

if __name__ == 'main':
  app.run(debug=True)