from lib2to3.pgen2 import token
from flask import jsonify, request, Blueprint
from controllers.result import result

result_module = Blueprint('result', __name__)
controller = result()

@result_module.get('/list')
def get_result():
    return jsonify(controller.get_all(request.args)), 200

@result_module.get('/<string:id>')
def show_result_by_id(id):
    return jsonify(controller.get_by_id(id))

@result_module.get('/table/<string:table>')
def show_result_by_table(table):
    return jsonify(controller.get_by_table_id(table))

@result_module.get('/candidate/<string:candidate>')
def show_result_by_candidate(candidate):
    return jsonify(controller.get_by_nombre(candidate))

@result_module.post('/<string:political_party_id>')
def create_result(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@result_module.put('/<string:id>')
def update_result(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@result_module.delete('/<string:id>')
def delete_result(id):
    controller.delete(id)
    return jsonify({}), 204