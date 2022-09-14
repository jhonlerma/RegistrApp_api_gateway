from lib2to3.pgen2 import token
from flask import jsonify, request, Blueprint
from controllers.table import table

table_module = Blueprint('table', __name__)
controller = table()

@table_module.get('/list')
def get_table():
    return jsonify(controller.get_all(request.args)), 200

@table_module.get('/<string:id>')
def show_table_by_id(id):
    return jsonify(controller.get_by_id(id))

@table_module.post('/<string:political_party_id>')
def create_table(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@table_module.put('/<string:id>')
def update_table(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@table_module.delete('/<string:id>')
def delete_table(id):
    controller.delete(id)
    return jsonify({}), 204