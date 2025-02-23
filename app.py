from flask import Flask, render_template, redirect, url_for
from flask import request

from db import db_methods


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/babylon")
def babylon_render():
    return render_template('babylon.html')

@app.route("/get_languages")
def get_languages():
    languages = db_methods.get_languages()
    print(languages)

@app.route("/post_language", methods = ["POST"])
def language_post():

    print("hola ruta")
    name = request.form['nombre']
    iso = request.form['iso']
    #dejamos pendiente el de countries por pedos de db

    characters = request.form['characters']
    #dejamos roots al lado por lo mismo que con los paises
    speakers = request.form['speakers']
    db_methods.add_language(name,iso,characters,speakers)

    return render_template('babylon.html')




if __name__ == ("__main__"):
    app.run(debug= True)
