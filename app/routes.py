from app import my_app
from flask import render_template, jsonify, url_for, request
from .db import update_fav, get_all_articles
from bson import ObjectId
import json


recent_filters = []
recent_link = {}
filt = {'fav': 0}
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
    global recent_link
    global recent_filters
    global filt
    recent_filters = []
    filt = {'fav': 0}
    active_link = {'index': 'active', 'fav': '', 'source': '', 'about': ''}
    recent_link = active_link
    articles = get_all_articles(filt=filt)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=active_link)

# FAVOURITE
@my_app.route('/fav')
def fav():
    global recent_link
    global recent_filters
    global filt
    recent_filters = []
    filt = {'fav': 1}
    active_link = {'index': '', 'fav': 'active', 'source': '', 'about': ''}
    recent_link = active_link
    articles = get_all_articles(filt=filt)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=active_link)

@my_app.route('/toggle_fav', methods=['POST'])
def toggle_fav():
    art_id = ObjectId(request.form.get('id'))
    fav = int(request.form.get('fav'))
    print(update_fav(art_id, fav))
    return jsonify({'success': True})

# FILTER
@my_app.route('/show_filter')
def show_filter():
    global recent_link
    global recent_filters
    articles = get_all_articles(filt=filt, text_classes=recent_filters)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=recent_link)

@my_app.route('/use_filters', methods=['POST'])
def use_filters():
    filter = json.loads(request.form.get('filter')) # обрабатываем json
    active_tab = request.form.get('active_tab')[:-5] # отсекаем "-link" из id ссылки
    global recent_link
    global recent_filters
    active_link = {'index': '', 'fav': '', 'source': '', 'about': ''}
    active_link[active_tab] = 'active'
    recent_link = active_link
    switches = {'switchPolitics': 'политика', 'switchEconomics': 'экономика', 'switchScience': 'наука', 'switchStrategy': 'ВС'}
    active_filt = []
    for key, value in filter.items():
        if value:
            active_filt.append(switches[key])
    recent_filters = active_filt
    print('recent_filter', recent_filters)
    print('recent_link', recent_link)
    return jsonify({'success': True})