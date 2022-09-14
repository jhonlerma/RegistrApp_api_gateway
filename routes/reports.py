from lib2to3.pgen2 import token
from flask import jsonify, request, Blueprint
from controllers.reports import reports

reports_module = Blueprint('reports', __name__)
controller = reports()

@reports_module.get('/list')
def get_reports():
    return jsonify(controller.get_all(request.args)), 200

@reports_module.get('/<string:id>')
def show_reports_by_id(id):
    return jsonify(controller.get_by_id(id))

@reports_module.post('/<string:political_party_id>')
def create_reports(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@reports_module.put('/<string:id>')
def update_reports(id):
    controller.update(id, request.get_json())
    return jsonify({}), 204

@reports_module.delete('/<string:id>')
def delete_reports(id):
    controller.delete(id)
    return jsonify({}), 204