from app import my_app
from flask import render_template, jsonify
from flask_pymongo import PyMongo


my_app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
mongo = PyMongo(my_app)

#Configuring collection name we are going to work with
#db_operations = mongo.db.<COLLECTION_NAME>
db_operations = mongo.db.users

#CRUD Operations

#Create

@my_app.route('/create')
def create():
    new_user = {'Name' : 'xyz', 'Age' : 20}
    db_operations.insert_one(new_user)
    #print(user['Name'],'Created successfully')
    result = {'result' : 'Created successfully'}
    return result

@my_app.route('/create-many')
def create_many():
    new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
    new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
    new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
    new_users = [new_user_1, new_user_2, new_user_3]
    db_operations.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

#Read

@my_app.route('/read')
def read():
    users = db_operations.find()
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)

@my_app.route('/read-with-filter')
def read_with_filter():
    filt = {'Name' : 'xyz'}
    users = db_operations.find(filt)
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)

@my_app.route('/read-one')
def read_one():
    filt = {'Name' : 'xyz'}
    user = db_operations.find_one(filt)
    output = {'Name' : user['Name'], 'Age' : user['Age']}
    #print(output)
    return jsonify(output)

#Update

@my_app.route('/update')
def update():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_one(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@my_app.route('/update-many')
def update_many():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_many(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@my_app.route('/update-if-exist-or-insert')
def update_if_exist_or_insert():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_one(filt, updated_user, upsert=True)
    result = {'result' : 'Done successfully'}
    return result

#Delete

@my_app.route('/delete')
def delete():
    filt = {'Name' : 'xyz'}
    db_operations.delete_one(filt)
    result = {'result' : 'Deleted successfully'}
    return result

@my_app.route('/delete-many')
def delete_many():
    filt = {'Name' : 'xyz'}
    db_operations.delete_many(filt)
    result = {'result' : 'Deleted successfully'}
    return result

@my_app.route('/')
@my_app.route('/index')
def index():
    return render_template("main.html")