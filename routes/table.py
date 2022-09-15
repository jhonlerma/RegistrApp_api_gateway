from flask import jsonify, request, Blueprint
from controllers.table import table
from decorators.token_decorator import role, token

table_module = Blueprint('table', __name__)
controller = table()

@table_module.get('/list')
@token
@role()
def get_table():
    return jsonify(controller.get_all(request.args)), 200

@table_module.get('/<string:id>')
@token
@role()
def show_table_by_id(id):
    return jsonify(controller.get_by_id(id))

@table_module.post('/<string:political_party_id>')
@token
@role()
def create_table(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@table_module.put('/<string:id>')
@token
@role()
def update_table(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@table_module.delete('/<string:id>')
@token
@role()
def delete_table(id):
    controller.delete(id)
    return jsonify({}), 204