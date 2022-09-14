from flask import Blueprint, jsonify, request
from controllers.table import table
from decorators.token_decorator import role, token

table_module = Blueprint("table",__name__)
controller = table()

@table_module.get('/')
@token
@role("adminitrator")
def get_results():
    return jsonify(controller.create(request.args.to_dict()))