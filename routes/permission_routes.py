from flask import jsonify, request, Blueprint
from controllers.permission_controller import PermissionController
from decorators.token_decorator import role, token

permission_module = Blueprint('permission', __name__)
controller = PermissionController()

@permission_module.get('​/api​/permissions')
@token
@role('administrator')
def getAllPermissions():
    return jsonify(controller.get_all(request.args)), 200