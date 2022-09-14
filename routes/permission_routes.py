from flask import jsonify, request, Blueprint
from controllers.permission_controller import PermissionController

candidate_module = Blueprint('candidate', __name__)
controller = PermissionController()


@candidate_module.get('​/api​/permissions')
def getAllPermissions():
    return jsonify(controller.get_all(request.args)), 200