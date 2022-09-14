from flask import Blueprint, jsonify, request
from controllers.reports import reports
from decorators.token_decorator import role, token

reports_module = Blueprint("reports",__name__)
controller = reports()

@reports_module.get('/list')
#@token
#@role("adminitrator")
#@role("jury")
#@role("cityzen")
def get_results():
    print("TODO VA BIEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    response, code = controller.get_all()
    return jsonify(response), code

@reports_module.get('/by_table')
@token
@role("adminitrator")
@role("jury")
@role("cityzen")
def get_reports_by_table():
    pass

@reports_module.get('/by_candidate')
@token
@role("adminitrator")
@role("jury")
@role("cityzen")
def get_reports_by_candidate():
    pass

@reports_module.get('/by_table_candidate')
@token
@role("adminitrator")
@role("jury")
@role("cityzen")
def get_reports_by_table_candidate():
    pass