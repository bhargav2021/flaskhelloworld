import numpy
from flask import Flask
import pandas
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application Success!'

if __name__ == '__main__':
  app.run()
