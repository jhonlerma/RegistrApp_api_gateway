from flask import jsonify, request, Blueprint
from controllers.permission_controller import PermissionController
from decorators.token_decorator import role, token

permissions_module = Blueprint('permission', __name__)
controller = PermissionController()

@permissions_module.get('/')
@token
@role()
def getAllPermissions():
    return jsonify(controller.get_all(request.args)), 200