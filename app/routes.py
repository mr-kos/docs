from app import my_app
from flask import render_template, jsonify, url_for, request
from .db import update_fav, get_all_articles
from bson import ObjectId


#NEWS API'S key
# 32a23ae7acf84154bc0c86c45a43c71f


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
    active_link = {'index': 'active', 'fav': '', 'source': '', 'about': ''}
    articles = get_all_articles(fav_mode=0)
    articles = [article.present() for article in articles]
    return render_template("main.html", art=articles, active_link=active_link)

@my_app.route('/fav')
def fav():
    active_link = {'index': '', 'fav': 'active', 'source': '', 'about': ''}
    articles = get_all_articles(fav_mode=1)
    articles = [article.present() for article in articles]
    return render_template("main.html", art=articles, active_link=active_link)

@my_app.route('/toggle_fav', methods=["POST"])
def toggle_fav():
    art_id = ObjectId(request.form.get("id"))
    fav = int(request.form.get("fav"))
    print(update_fav(art_id, fav))
    return jsonify({"success": True})
