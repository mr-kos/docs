from app import my_app
from flask import render_template, jsonify, request
from .db import update_fav, get_all_articles
from bson import ObjectId
import json, requests


recent_filters = []
recent_link = {'index': 'active', 'fav': '', 'source': '', 'about': ''}
filt = {'fav': 0}
switches_state = {'switchPolitics': '', 'switchEconomics': '', 'switchScience': '', 'switchStrategy': ''}
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
    global switches_state

    recent_filters = []
    filt = {'fav': 0}
    active_link = {'index': 'active', 'fav': '', 'source': '', 'about': ''}
    switches_state = {'switchPolitics': '', 'switchEconomics': '', 'switchScience': '', 'switchStrategy': ''}
    recent_link = active_link

    articles = get_all_articles(filt=filt)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=active_link, switches_state=switches_state)

# FAVOURITE
@my_app.route('/fav')
def fav():
    global recent_link
    global recent_filters
    global filt
    global switches_state

    recent_filters = []
    filt = {'fav': 1}
    active_link = {'index': '', 'fav': 'active', 'source': '', 'about': ''}
    switches_state = {'switchPolitics': '', 'switchEconomics': '', 'switchScience': '', 'switchStrategy': ''}
    recent_link = active_link

    articles = get_all_articles(filt=filt)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=active_link, switches_state=switches_state)

@my_app.route('/toggle_fav', methods=['POST'])
def toggle_fav():
    art_id = ObjectId(request.form.get('id'))
    fav = int(request.form.get('fav'))
    print(update_fav(art_id, fav))
    return jsonify({'success': True})

# FILTER
@my_app.route('/show_filter')
def show_filter():
    articles = get_all_articles(filt=filt, text_classes=recent_filters)
    articles = [article.present() for article in articles]
    return render_template('main.html', art=articles, active_link=recent_link, switches_state=switches_state)

@my_app.route('/use_filters', methods=['POST'])
def use_filters():
    filter = json.loads(request.form.get('filter')) # обрабатываем json
    active_tab = request.form.get('active_tab')[:-5] # отсекаем "-link" из id ссылки
    global recent_link
    global recent_filters
    global switches_state
    active_link = {'index': '', 'fav': '', 'source': '', 'about': ''}
    active_link[active_tab] = 'active'
    recent_link = active_link
    switches = {'switchPolitics': 'политика', 'switchEconomics': 'экономика', 'switchScience': 'наука', 'switchStrategy': 'ВС'}
    active_filt = []
    for key, value in filter.items():
        if value:
            active_filt.append(switches[key])
            switches_state[key] = 'checked' # for switches state in layout
        else:
            switches_state[key] = ''

    recent_filters = active_filt

    return jsonify({'success': True})

#News API key 32a23ae7acf84154bc0c86c45a43c71f

#SOURCE
@my_app.route('/source')
def source():
    switches_state = {'switchPolitics': '', 'switchEconomics': '', 'switchScience': '', 'switchStrategy': ''}
    active_link = {'index': '', 'fav': '', 'source': 'active', 'about': ''}
    recent_link = active_link
    return render_template('source.html', art=[], active_link=recent_link, switches_state=switches_state)

# FILTER
@my_app.route('/show_source_articles')
def show_source_articles():
    url = ('https://newsapi.org/v2/top-headlines?'
       'language=en&'
       'category=general&'
       'from=2022-01-21&'
       'sortBy=popularity&'
       'apiKey=32a23ae7acf84154bc0c86c45a43c71f')

    response = requests.get(url)
    print(response.json())

    return "OK"


#ABOUT
@my_app.route('/about')
def about():
    switches_state = {'switchPolitics': '', 'switchEconomics': '', 'switchScience': '', 'switchStrategy': ''}
    active_link = {'index': '', 'fav': '', 'source': '', 'about': 'active'}
    recent_link = active_link
    return render_template('main.html', art=[], active_link=recent_link, switches_state=switches_state)