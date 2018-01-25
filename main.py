import joblib
import numpy
from flask import Flask, render_template,request
import pandas
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
  return render_template("values.html")


@app.route('/predict', methods=['POST'])
def predict():
   clf  = joblib.load("two_values_model.pkl")
   m =clf.predict([[value , 2nd value]])
   return m

if __name__ == '__main__':
  app.run()
