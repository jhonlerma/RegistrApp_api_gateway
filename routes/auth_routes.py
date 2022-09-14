
from flask import Blueprint, jsonify, request

from controllers.auth_controller import AuthContoller



auth_module =Blueprint("auth",__name__)

controller =AuthContoller()


@auth_module.post('/')
def login():
  response, code = controller.login(request.get_json())
  return jsonify(response), code