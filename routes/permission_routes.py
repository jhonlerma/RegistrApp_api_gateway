from flask import jsonify, request, Blueprint
from controllers.permission_controller import PermissionController

permission_module = Blueprint('permission', __name__)
controller = PermissionController()


@permission_module.get('​/api​/permissions')
def getAllPermissions():
    return jsonify(controller.get_all(request.args)), 200