from flask import Blueprint, jsonify, request
from controllers.table import table
from decorators.token_decorator import role, token

table_module = Blueprint("table",__name__)
controller = table()

@table_module.post('/')
@token
@role("Admin")
def create():
  response, code = controller.create(request.get_json())
  return jsonify(response), code
  # return jsonify({}), 200