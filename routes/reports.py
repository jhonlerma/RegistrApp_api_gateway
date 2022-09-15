from flask import jsonify, request, Blueprint
from controllers.reports import reports
from decorators.token_decorator import role, token

reports_module = Blueprint('reports', __name__)
controller = reports()

@reports_module.get('/')
@token
@role()
def get_reports():
    return jsonify(controller.get_all(request.args.to_dict())), 200

@reports_module.get('/by_table')
@token
@role()
def by_table():
    return jsonify(controller.get_by_table(request.args.to_dict())),200

@reports_module.get('/by_candidate')
@token
@role()
def by_candidate():
    return jsonify(controller.get_by_candidate(request.args.to_dict())), 200

@reports_module.get('/by_table_candidate')
@token
@role()
def by_table_candidate():
    controller.get_by_table_candidate(request.args.to_dict()), 200
    return jsonify({}), 204
