from flask import jsonify, request, Blueprint
from controllers.result import result
from decorators.token_decorator import role, token

result_module = Blueprint('result', __name__)
controller = result()

@result_module.get('/list')
@token
@role('administrator')
def get_result():
    return jsonify(controller.get_all(request.args)), 200

@result_module.get('/<string:id>')
@token
@role('administrator')
def show_result_by_id(id):
    return jsonify(controller.get_by_id(id))
@result_module.get('/table/<string:table>')
@token
@role('administrator')
def show_result_by_table(table):
    return jsonify(controller.get_by_table_id(table))

@result_module.get('/candidate/<string:candidate>')
@token
@role('administrator')
def show_result_by_candidate(candidate):
    return jsonify(controller.get_by_nombre(candidate))

@result_module.post('/<string:political_party_id>')
@token
@role('administrator')
def create_result(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@result_module.put('/<string:id>')
@token
@role('administrator')
def update_result(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@result_module.delete('/<string:id>')
@token
@role('administrator')
def delete_result(id):
    controller.delete(id)
    return jsonify({}), 204