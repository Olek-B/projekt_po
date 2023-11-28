from flask import Flask,request,jsonify,json
from flask_cors import CORS
from definitions import get_data,insert_user, remove_user,patch_user,check_data

app = Flask(__name__)


@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(get_data())

@app.route("/users",methods=['POST'])
def add_users():
    insert_user(request.json)
    return "", 201

@app.route("/users/<int:user_id>",methods=['GET'])
def get_user_by_id(user_id):
    return get_data(user_id)

@app.route("/users/<int:user_id>",methods=['PATCH'])
def patch_user_by_id(user_id):
    if check_data():
        patch_user(user_id,request.json)
        return '', 204
    else:
        return '', 400

@app.route("/users/<int:user_id>",methods=['PUT'])
def update_user_by_id(user_id):
    a=get_data()
    if any(obj['id'] == user_id for obj in a):
        patch_user(user_id,request.json)
    else:
        insert_user(request.json,user_id)
    return '',204

@app.route("/users/<int:user_id>",methods=['DELETE'])
def remove_user_by_id(user_id):
    if any(obj['id'] == user_id for obj in get_data()):
        remove_user(user_id)
        return "", 204
    else:
        return '', 400