
import joblib
import numpy
from flask import Flask, render_template,request
import pandas
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template(values.html)


@app.route('/predict')
def predict():
   clf  = joblib.load(models_dir + model + "/" + model + ".pkl")
   m =clf.predict([[1st value , 2nd value]])
   return m




if __name__ == '__main__':
  app.run()
