from flask import jsonify, request, Blueprint
from controllers.user_controller import UsersController
from decorators.token_decorator import token, role

users_module = Blueprint('users', __name__)
controller = UsersController()

@token
@role('administrator')
@users_module.get('/')
def get_all():
    return jsonify(controller.get_all(request.args)), 200

@token
@role('administrator')
@users_module.get('/<string:id>')
def show_user_by_id(id):
    return jsonify(controller.get_by_id(id))

@token
@role('administrator')    
@users_module.post('/')
def create_user():
    return jsonify(controller.create(request.get_json())), 200

@token
@role('administrator')    
@users_module.delete('/<string:id>')
def delete_user_by_id(id):
    controller.delete_by_id(id)
    return jsonify({}),204

@token
@role('administrator')
@users_module.put('/<string:id>')
def update_user(id):
    print("print",id, request.get_json())   
    controller.update(id, request.get_json()),200   
    return {},204  

@token
@role('administrator')
@users_module.get('/roles/<string:role>')
def show_user_by_rol(role):
    return jsonify(controller.get_by_rol(role))

