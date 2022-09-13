from flask import Blueprint, jsonify, request
from controllers.reports import reports
from decorators.token_decorator import role, token

reports_module = Blueprint("reports",__name__)
controller = reports()

@reports_module.post('/')
@token
@role("Admin")
def create():
  response, code = controller.create(request.get_json())
  return jsonify(response), code
  # return jsonify({}), 200