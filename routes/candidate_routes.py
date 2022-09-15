from flask import jsonify, request, Blueprint
from controllers.candidate_controller import CandidateController
from decorators.token_decorator import role, token

candidate_module = Blueprint('candidate', __name__)
controller = CandidateController()

@candidate_module.get('/list')
@token
@role()
def get_candidates():
    return jsonify(controller.get_all(request.args)), 200

@candidate_module.get('/<string:id>')
@token
@role()
def show_candidate_by_id(id):
    return jsonify(controller.get_by_id(id))

@candidate_module.get('/document/<string:document>')
@token
@role()
def show_candidate_by_document(document):
    return jsonify(controller.get_by_document_id(document))

@candidate_module.get('/resolution/<string:resolution>')
@token
@role()
def show_candidate_by_resolution(resolution):
    return jsonify(controller.get_by_resolution(resolution))

@candidate_module.post('/<string:political_party_id>')
@token
@role()
def create_candidate(political_party_id):
    return jsonify(controller.create(request.get_json(), political_party_id)), 201

@candidate_module.put('/<string:id>')
@token
@role()
#@role("Admin")
def update_candidate(id):
    response,code = controller.update(id,request.get_json())
    return jsonify(response),code

@candidate_module.delete('/<string:id>')
@token
@role()
def delete_candidate(id):
    controller.delete(id)
    return jsonify({}), 204