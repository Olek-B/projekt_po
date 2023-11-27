from flask import Flask,request,jsonify,json
from flask_cors import CORS
from definitions import get_data,insert_user, remove_user,patch_user

app = Flask(__name__)


@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(get_data())

@app.route("/users",methods=['POST'])
def add_users():
    insert_user(request.json)
    return "Success", 201

@app.route("/users/<int:user_id>")
def get_user_by_id(user_id):
    return get_data(user_id)

@app.route("/users/<int:user_id>",methods=['PATCH'])
def patch_user_by_id(user_id):
    patch_user(user_id,request.json)
    return "s",204


@app.route("/users/<int:user_id>",methods=['DELETE'])
def remove_user_by_id(user_id):
    remove_user(user_id)
    return "Success", 204