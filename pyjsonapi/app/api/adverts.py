from app.api import bp
from flask import jsonify
from app.models import Advert
from flask import request
from app import db
from app.api.errors import bad_request, error_response
from sqlalchemy import text


@bp.route('/get_advert/<int:id>', methods=['GET'])
def get_advert(id):
    return jsonify(Advert.query.get_or_404(id).to_dict())

@bp.route('/get_all_adverts/', methods=['GET'])
def get_all_adverts():
	data = request.get_json() or {}
	page = request.args.get('page', 1, type=int)

	sorting_fields = []
	if 'sort_date' in data:
		if data['sort_date'] == 'asc':
			sorting_fields.append('timestamp')
		elif data['sort_date'] == 'desc':
			sorting_fields.append('timestamp desc')
	
	if 'sort_price' in data:
		if data['sort_price'] == 'asc':
			sorting_fields.append('price')
		elif data['sort_price'] == 'desc':
			sorting_fields.append('price desc')
	criteria = ", ".join(sorting_fields)
			
	return jsonify(Advert.to_collection_dict(Advert.query, page, 'api.get_all_adverts', text(criteria)))

@bp.route('/create_advert/', methods=['POST'])
def create_advert():
	data = request.get_json() or {}
	if 'head' not in data or 'content' not in data or \
	   'price' not in data or 'photo1' not in data:
		return bad_request('request must have all the fileds: head, content, price and main photo')
	a = Advert()
	a.from_dict(data)
	db.session.add(a)
	db.session.commit()
	response = {}
	response['id'] = a.id
	response['code'] = 201
	response = jsonify(response)
	response.status_code = 201
    #response.headers['Location'] = url_for('api.get_user', id=a.id)
	return response

