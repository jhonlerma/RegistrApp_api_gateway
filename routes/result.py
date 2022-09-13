from flask import Blueprint, jsonify, request
from controllers.result import result
from decorators.token_decorator import role, token

result_module = Blueprint("result",__name__)
controller = result()

@result_module.post('/')
@token
@role("Admin")
def create():
  response, code = controller.create(request.get_json())
  return jsonify(response), code
  # return jsonify({}), 200