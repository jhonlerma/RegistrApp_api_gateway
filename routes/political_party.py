from flask import jsonify, request, Blueprint
from controllers.political_party import political_party
from decorators.token_decorator import role, token

political_party_module = Blueprint('political_party', __name__)
controller = political_party()

@political_party_module.get('/list')
@token
@role()
def get_political_party():
    return jsonify(controller.get_all(request.args)), 200

@political_party_module.get('/<string:id>')
@token
@role()
def show_political_party_by_id(id):
    return jsonify(controller.get_by_id(id))

@political_party_module.get('/lema/<string:lema>')
@token
@role()
def show_political_party_by_lema(lema):
    return jsonify(controller.get_by_lema_id(lema))

@political_party_module.get('/nombre/<string:nombre>')
@token
@role()
def show_political_party_by_nombre(nombre):
    return jsonify(controller.get_by_nombre(nombre))

@political_party_module.post('/<string:political_party_id>')
@token
@role()
def create_political_party(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@political_party_module.put('/<string:id>')
@token
@role()
def update_political_party(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@political_party_module.delete('/<string:id>')
@token
@role()
def delete_political_party(id):
    controller.delete(id)
    return jsonify({}), 204