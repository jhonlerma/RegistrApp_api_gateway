from flask import jsonify, request, Blueprint
from controllers.role_permission_controller import RolePermissionController

role_permission_module = Blueprint('role_permission', __name__)
controller = RolePermissionController()


@role_permission_module.get('​/api​/role_permissions')
def getAllRolePermissions():
    return jsonify(controller.get_all(request.args)), 200