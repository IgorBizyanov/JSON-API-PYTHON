from datetime import datetime
from app import db
from flask import url_for


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, endpoint, *sort_criterion, **kwargs):
        resources = query.order_by(*sort_criterion).paginate(page, 10, False)
        
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'next': url_for(endpoint, page=page + 1,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, 
                                **kwargs) if resources.has_prev else None
            }
        }
        return data	


class Advert(PaginatedAPIMixin, db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	head = db.Column(db.String(200))
	content = db.Column(db.String(1000))
	price = db.Column(db.Float(), default=0)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	photo1 = db.Column(db.String(200), default='')
	photo2 = db.Column(db.String(200), default='')
	photo3 = db.Column(db.String(200), default='')

	def __repr__(self):
		return '<Advert {}>'.format(self.head)

	def to_dict(self):
		data = {
			'id': self.id,
			'head': self.head,
			'content': self.content,
			'price': self.price,
			'datetime': self.timestamp.isoformat(' '),
			'photo': self.photo1
		}
		return data

	def from_dict(self, data):
		for field in ['head', 'content', 'price', 'photo1', 'photo2', 'photo3']:
			if field in data:
				setattr(self, field, data[field])
