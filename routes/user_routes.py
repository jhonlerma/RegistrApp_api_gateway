from flask import jsonify, request, Blueprint
from controllers.user_controller import UsersController
from decorators.token_decorator import role, token

users_module = Blueprint('users', __name__)
controller = UsersController()

@users_module.get('/')
@token
@role('administrator')
def get_all():
    return jsonify(controller.get_all(request.args)), 200

@users_module.get('/<string:id>')
@token
@role('administrator')
def show_user_by_id(id):
    return jsonify(controller.get_by_id(id))

@users_module.post('/')
@token
@role('administrator')    
def create_user():
    return jsonify(controller.create(request.get_json())), 200

@users_module.delete('/<string:id>')
@token
@role('administrator')    
def delete_user_by_id(id):
    controller.delete_by_id(id)
    return jsonify({}),204

@users_module.put('/<string:id>')
@token
@role('administrator')
def update_user(id):
    print("print",id, request.get_json())   
    controller.update(id, request.get_json()),200   
    return {},204  

@users_module.get('/roles/<string:role>')
@token
@role('administrator')
def show_user_by_rol(role):
    return jsonify(controller.get_by_rol(role))

