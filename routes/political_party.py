from lib2to3.pgen2 import token
from flask import jsonify, request, Blueprint
from controllers.political_party import political_party

political_party_module = Blueprint('political_party', __name__)
controller = political_party()

@political_party_module.get('/list')
def get_political_party():
    return jsonify(controller.get_all(request.args)), 200

@political_party_module.get('/<string:id>')
def show_political_party_by_id(id):
    return jsonify(controller.get_by_id(id))

@political_party_module.get('/lema/<string:lema>')
def show_political_party_by_lema(lema):
    return jsonify(controller.get_by_lema_id(lema))

@political_party_module.get('/nombre/<string:nombre>')
def show_political_party_by_nombre(nombre):
    return jsonify(controller.get_by_nombre(nombre))

@political_party_module.post('/<string:political_party_id>')
def create_political_party(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@political_party_module.put('/<string:id>')
def update_political_party(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@political_party_module.delete('/<string:id>')
def delete_political_party(id):
    controller.delete(id)
    return jsonify({}), 204