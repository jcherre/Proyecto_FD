
import os
from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import MongoClient
import aws_rekog
import nlu
import tweeter_scraping
import youtube_scraping
import json


try:
    client = MongoClient('localhost',27017)
    db = client.myappdb
    proyectos = db.proyectos
    print('done')
    client.server_info()
except:
    print("Error - Cannot coneect to db")

app = Flask(__name__)

#app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
#mongo = PyMongo(app)
#client = MongoClient(os.environ['MONGODB_HOSTNAME'],27017,username=os.environ['MONGODB_USERNAME'],password=os.environ['MONGODB_PASSWORD'])
#@app.route('/', methods=('GET', 'POST'))

# FUNCIONES ################
#@app.route('/scrap', methods=['POST'])
def scrap(_id):
    if request.method == 'POST':
        res = tweeter_scraping.twitterFind(request.form['mainPalabra'].lower(),request.form['tags'].split(' '))
        print(json.dumps(res,indent=2))
        proyectos.update_one({'_id':_id.inserted_id},{"$set":{"twitter":res}})
    return redirect('/')



############################


@app.route('/', methods=('GET', 'POST'))
def create():
    print('into function create')
    if (request.method == "POST") and (request.form['mainPalabra'] != '') and (request.form['mainPalabra'] != ''):
        nombre = request.form['nombre']
        mainPalabra = request.form['mainPalabra']
        imagen = request.form['imagen']
        tags = request.form['tags'].split(' ')
        _id = proyectos.insert_one({
            'nombre': nombre, 'mainPalabra':mainPalabra, 'tags': tags, 'imagen': imagen
        })
        scrap(_id)
        print('added to db')
    else:
        print('no completado')
    all_proyectos = proyectos.find()

    return render_template('index.html', proyectos = all_proyectos)


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
