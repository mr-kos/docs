from app import my_app
from .article import Article
from flask_pymongo import PyMongo
from bson import ObjectId


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


def read_all():
    if db_operations.count != 0:
        articles = db_operations.find()
        output = [{'art_id': article['_id'], 
                'abstr' : article['abstr'], 
                'text_class' : article['text_class'], 
                'text' : article['text'], 
                'time': article['time'], 
                'fav': article['fav']} for article in articles]
        return output
    else:
        return "No articles"

def read(only_fav=False):
    if db_operations.count != 0:
        results = []
        if only_fav:
            filt = {'fav': 1}
            results = db_operations.find(filt)
        else:
            results = db_operations.find()
        output = [Article(item['_id'], item['abstr'], item['text'], item['text_class'], item['time'], item['fav']) for item in results]
        return output
    else:
        return []

# DEPRECATED
# def read_all():
#     if db_operations.count != 0:
#         articles = db_operations.find()
#         output = [{'art_id': article['_id'], 
#                 'abstr' : article['abstr'], 
#                 'text_class' : article['text_class'], 
#                 'text' : article['text'], 
#                 'time': article['time'], 
#                 'fav': article['fav']} for article in articles]
#         return output
#     else:
#         return "No articles"

# DEPRECATED
# def get_fav():
#     if db_operations.count != 0:
#         filt = {'fav': 1}
#         articles = db_operations.find(filt)
#         output = [{'abstr' : article['abstr'], 'text_class' : article['text_class'], 
#                     'text' : article['text'], 'time': article['time'], 'fav': article['fav']} 
#                 for article in articles]
#         return output
#     else:
#         return "No articles"


def update_fav(art_id, new_fav):
    updated_art = {"$set": {'fav' : int(new_fav)}}
    filt = {'_id' : ObjectId(art_id)}
    db_operations.update_one(filt, updated_art, upsert=False)
    print("Updated!")
    return 0