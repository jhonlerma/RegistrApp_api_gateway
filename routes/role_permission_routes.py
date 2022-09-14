from flask import jsonify, request, Blueprint
from controllers.role_permission_controller import RolePermissionController

candidate_module = Blueprint('candidate', __name__)
controller = RolePermissionController()


@candidate_module.get('​/api​/role_permissions')
def getAllRolePermissions():
    return jsonify(controller.get_all(request.args)), 200