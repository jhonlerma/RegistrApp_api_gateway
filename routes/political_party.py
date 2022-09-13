from flask import Blueprint, jsonify, request
from controllers.political_party import political_party
from decorators.token_decorator import role, token

political_party_module = Blueprint("political_party",__name__)
controller = political_party()

@political_party_module.post('/')
@token
@role("Admin")
def create():
  response, code = controller.create(request.get_json())
  return jsonify(response), code
  # return jsonify({}), 200