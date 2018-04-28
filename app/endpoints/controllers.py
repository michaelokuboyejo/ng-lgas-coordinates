from app.endpoints.models import LGA
from flask import Blueprint, Response
from json import dumps

__author__ = 'michaelokuboyejo'

endpoints = Blueprint('api/v1', __name__, url_prefix='/api/v1')


@endpoints.route('/lgas/<string:state_code_or_state>', methods=['GET'])
def get_lga_in_state(state_code_or_state):
    lga_data = LGA.get_lga_with_state_name_or_code(state_code_or_state)
    if lga_data is None:
        return {'error': 'Data not Found'}, 404 # handle 404
    else:
        return Response(dumps(lga_data), mimetype='application/json')


@endpoints.route('/lgas', methods=['GET'])
def get_lgas():
    lgas = LGA.get_lgas()
    return Response(dumps(lgas), mimetype='application/json')