from app import my_app
from .article import Article
from flask import render_template, jsonify, url_for, request
# from flask_pymongo import PyMongo
from datetime import date, datetime
from bson import ObjectId
from .db import db_operations, update_fav, read
from app import article

# @my_app.route('/create')
# def create():
#     article = {
#         'abstr' : 'Сompletion of three major pi is ramping up capital expenditure.',
#         'text_class' : 'наука',
#         'text' : 'Сircumventing pipeline three majorcircumventing pipeline transit via Ukraine. This involves the construction or completion of three major pipelines that will connect Russia directly with its largest demand markets. Power of Siberia (to China), TurkStream (to Turkey) and Nord Stream II (to Germany).',
#         'time' : datetime.today().replace(microsecond=0),
#         'fav': int(1)
#         }
#     db_operations.insert_one(article)
#     result = {'result' : 'Created successfully'}
#     return result

@my_app.route('/')
@my_app.route('/index')
def index():
    articles = read()
    articles = [article.present() for article in articles]
    return render_template("main.html", art=articles)

@my_app.route('/fav')
def fav():
    articles = read(only_fav=True)
    articles = [article.present() for article in articles]
    return render_template("main.html", art=articles)

@my_app.route('/toggle_fav', methods=["POST"])
def toggle_fav():
    art_id = request.form.get("id")
    fav = request.form.get("fav")
    update_fav(art_id, fav)
    return jsonify({"success": True})
