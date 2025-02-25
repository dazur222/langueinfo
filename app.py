from flask import Flask, render_template, redirect, url_for, jsonify
from flask import request

from db import db_methods


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/babylon")
def babylon_render():
    return render_template('babylon.html')

@app.route("/language_compare")
def language_compare_render():
    return render_template('languagecompare.html')

@app.route("/get_languages", methods = ['GET'])
def get_languages():
        
    try:
        languages = db_methods.get_languages()
        return jsonify(languages)

    except Exception as e:
        print(e)

  

@app.route("/post_language", methods = ["POST"])
def post_language():
    try:

        req = request.json
        print("el req es",req)

        name = req['name']
        iso = req['iso']
        characters = req['characters']
        speakers = req['speakers']

        language = db_methods.add_language(name,iso,characters,speakers,0)
        print(language)
        return jsonify(language)
    
    except Exception as e:
        print(e)

@app.route("/get_similarities", methods = ["POST"])
def get_similarities():
    try:
        req = request.json

        lang_a = req['lang_a']
        lang_b = req['lang_b']

        similarites = similarities(lang_a,lang_b)
        print(similarites)
        return jsonify(similarites)
        
    except Exception as e:
        print(e)


def similarities(language_a,language_b):
    #recibe un diccionario con los datos de los dos lenguajes
   
    char_set_a = set(language_a['characters'])
    char_set_b = set(language_b['characters'])

    sim = char_set_a.intersection(char_set_b)


    if sim != set():
        full = 100
        val = 100 / len(char_set_a)
        for char in char_set_a:
            if char not in sim:
                full = full - val
        sim = sorted(sim)
        return { 'percentage' : round(full,2), 'similarities' : sim}
    else:
        return {'similarities' : "no similarities"}
   




if __name__ == ("__main__"):
    app.run(debug= True)
