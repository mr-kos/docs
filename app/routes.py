from app import my_app
from flask import render_template, jsonify, url_for, request
from flask_pymongo import PyMongo
from datetime import date, datetime
from bson import ObjectId


my_app.config["MONGO_URI"] = "mongodb://localhost:27017/docs"
mongo = PyMongo(my_app)

#Configuring collection name we are going to work with
#db_operations = mongo.db.<COLLECTION_NAME>
db_operations = mongo.db.articles
# db_operations = mongo.db.articles.drop()

#CRUD Operations

#Create

def read_art():

    if mongo.db.articles.count != 0:
        articles = db_operations.find()
        output = [{'art_id': article['_id'], 
                'abstr' : article['abstr'], 
                'text_class' : article['text_class'], 
                'text' : article['text'], 
                'time': article['time'], 
                'fav': article['fav']} for article in articles]
        print([item["fav"] for item in output])
        return output
    else:
        return "No articles"

def update(id, new_fav):
    updated_art = {"$set": {'fav' : int(new_fav)}}
    filt = {'_id' : ObjectId(id)}
    out = db_operations.find({'_id': ObjectId(id)})
    print("before:  " + str(list(out)[0]["fav"]))
    db_operations.update_one(filt, updated_art, upsert=False)
    out = db_operations.find({'_id': ObjectId(id)})
    print("after:  " + str(list(out)[0]["fav"]))
    print("Updated!")
    return 0

def get_fav():
    if mongo.db.articles.count != 0:
        articles = db_operations.find({'fav': 1})
        output = [{'abstr' : article['abstr'], 'text_class' : article['text_class'], 
                    'text' : article['text'], 'time': article['time'], 'fav': article['fav']} 
                for article in articles]
        return output
    else:
        return "No articles"

@my_app.route('/create')
def create():
    article = {
        'abstr' : 'Сompletion of three major pi is ramping up capital expenditure.',
        'text_class' : 'наука',
        'text' : 'Сircumventing pipeline three majorcircumventing pipeline transit via Ukraine. This involves the construction or completion of three major pipelines that will connect Russia directly with its largest demand markets. Power of Siberia (to China), TurkStream (to Turkey) and Nord Stream II (to Germany).',
        'time' : datetime.today().replace(microsecond=0),
        'fav': int(1)
        }
    db_operations.insert_one(article)
    result = {'result' : 'Created successfully'}
    return result

# @my_app.route('/create-many')
# def create_many():
#     new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
#     new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
#     new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
#     new_users = [new_user_1, new_user_2, new_user_3]
#     db_operations.insert_many(new_users)
#     result = {'result' : 'Created successfully'}
#     return result

#Read

@my_app.route('/read')
def read():
    articles = db_operations.find()
    output = [{'abstract' : article['Abstract'], 'class' : article['Class'], 'full' : article['Full']} for article in articles]
    print(output[0])
    return render_template("main.html", art=output[0])


# @my_app.route('/read-one')
# def read_one():
#     filt = {'Name' : 'xyz'}
#     user = db_operations.find_one(filt)
#     output = {'Name' : user['Name'], 'Age' : user['Age']}
#     #print(output)
#     return jsonify(output)


# @my_app.route('/delete')
# def delete():
#     filt = {'Name' : 'xyz'}
#     db_operations.delete_one(filt)
#     result = {'result' : 'Deleted successfully'}
#     return result

# @my_app.route('/delete-many')
# def delete_many():
#     filt = {'Name' : 'xyz'}
#     db_operations.delete_many(filt)
#     result = {'result' : 'Deleted successfully'}
#     return result

@my_app.route('/')
@my_app.route('/index')
def index():
    articles = read_art()
    print(articles[0]['art_id'])
    return render_template("main.html", art=articles)

@my_app.route('/fav')
def fav():
    articles = get_fav()
    return render_template("main.html", art=articles)

@my_app.route('/toggle_fav', methods=["POST"])
def toggle_fav():
    art_id = request.form.get("id")
    fav = request.form.get("fav")
    update(art_id, fav)
    return jsonify({"success": True})
