from flask import jsonify, request, Blueprint
from controllers.role_controller import RoleController
from decorators.token_decorator import token , role

roles_module = Blueprint('roles', __name__)
controller = RoleController()

@token
@role('administrator')
@roles_module.get('/')
def get_all():
    return jsonify(controller.get_all(request.args)), 200
@token
@role('administrator')
@roles_module.get('/<string:role>')
def show_user_by_rol(role):
    return jsonify(controller.get_by_rol(role))