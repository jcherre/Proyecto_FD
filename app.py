import os
from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
#app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

#mongo = PyMongo(app)
client = MongoClient(os.environ['MONGODB_HOSTNAME'],27017,username=os.environ['MONGODB_USERNAME'],password=os.environ['MONGODB_PASSWORD'])
db = client.myappdb
estudiantes = db.estudiantes

@app.route('/', methods=('GET', 'POST'))

def index():
    all_estudiantes = estudiantes.find()
    return render_template('index.html', estudiantes=all_estudiantes)

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
