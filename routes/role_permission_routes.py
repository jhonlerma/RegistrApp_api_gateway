from flask import jsonify, request, Blueprint
from controllers.role_permission_controller import RolePermissionController
from decorators.token_decorator import role, token

role_permissions_module = Blueprint('role_permission', __name__)
controller = RolePermissionController()

@role_permissions_module.get('/')
@token
@role()
def getAllRolePermissions():
    return jsonify(controller.get_all(request.args)), 200