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

@app.route("/get_languages", methods = ['GET'])
def get_languages():
        
    try:
        languages = db_methods.get_languages()
        return jsonify(languages)

    except Exception as e:
        print(e)

  

# try:

# except Exception as e:
#     print(e)

@app.route("/post_language", methods = ["POST"])
def language_post():
    try:

        req = request.json
        print("el req es",req)

        name = req['name']
        iso = req['iso']
        characters = req['characters']
        speakers = req['speakers']

        language = db_methods.add_language(name,iso,characters,speakers)
        print(language)
        return jsonify(language)
    
    except Exception as e:
        print(e)

    




if __name__ == ("__main__"):
    app.run(debug= True)
