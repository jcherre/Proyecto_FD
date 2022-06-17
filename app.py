from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017, username='userdemo', password='Tecsup')
db = client.myappdb
estudiantes = db.estudiantes

@app.route('/', methods=('GET', 'POST'))

def index():
    all_estudiantes = estudiantes.find()
    return render_template('index.html', estudiantes=all_estudiantes)

if __name__ == "__main__":
    app.run(debug=True)
