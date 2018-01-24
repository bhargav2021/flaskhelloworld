from flask import Flask
from numpy import numpy
from pandas import pandas
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'

if __name__ == '__main__':
  app.run()
