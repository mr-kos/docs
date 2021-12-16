from app import my_app
from .article import Article
from flask_pymongo import PyMongo
from copy import deepcopy


my_app.config["MONGO_URI"] = "mongodb://localhost:27017/docs"
mongo = PyMongo(my_app)
db_operations = mongo.db.articles
# db_operations = mongo.db.articles.drop()


#     db_operations.delete_one(filt)
#     db_operations.delete_many(filt)
#     user = db_operations.find_one(filt)
#     user = db_operations.find(filt)
#     db_operations.insert_one(article)
#     db_operations.insert_many(new_users)

# def create_many():
#     new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
#     new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
#     new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
#     new_users = [new_user_1, new_user_2, new_user_3]
#     db_operations.insert_many(new_users)
#     result = {'result' : 'Created successfully'}
#     return result

def get_all_articles(filt, text_classes=[]):
    # fav_mode
    # 0 - only unfavourite
    # 1 - only favourite
    # 2 - all
    if db_operations.count != 0:
        results = []
        filter = deepcopy(filt)
        
        if len(text_classes) > 0:
            filter['text_class'] = {'$in': text_classes}

        results = db_operations.find(filter)
        output = [parse_article(item) for item in results]
        return output
    else:
        return []

def parse_article(dict):
    article = Article(dict['_id'], dict['abstr'], dict['text'], dict['text_class'], dict['time'], fav=dict['fav'])
    return article

def get_article(filt):
    if db_operations.count != 0:
        result = db_operations.find_one(filt)
        return parse_article(result)

def update_db(article):
    filt = {'_id' : article.id}
    updated_art = {
        "$set": {'fav' : article.fav}
        }
    db_operations.update_one(filt, updated_art, upsert=False)
    return 0


def update_fav(art_id, new_fav):
    filt = {'_id' : art_id}
    article = get_article(filt)
    article.fav = new_fav
    res = update_db(article)
    if res == 0:
        return 'Success'
    else:
        return 'Fail'