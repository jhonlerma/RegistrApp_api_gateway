
from flask import Blueprint, jsonify, request
from decorators.token_decorator import token
from controllers.auth_controller import AuthContoller



auth_module =Blueprint("auth",__name__)

controller =AuthContoller()


@auth_module.post('/')
def login():
  response, code = controller.login(request.get_json())
  return jsonify(response), code

@auth_module.get('/me')
@token
def me():
  response, code = controller.me(request.args['user_id']['id'])
  print(request.args)
  return jsonify(response), code