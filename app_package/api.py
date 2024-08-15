from flask import Blueprint, jsonify, request
from .models import db, Status

api = Blueprint('api', __name__)

@api.route('/statuses', methods=['GET'])
def get_statuses():
    statuses = Status.query.all()
    return jsonify([status.to_dict() for status in statuses])

@api.route('/statuses', methods=['POST'])
def add_status():
    data = request.json
    new_status = Status(name=data['name'])
    db.session.add(new_status)
    db.session.commit()
    return jsonify(new_status.to_dict()), 201

@api.route('/statuses/<int:id>', methods=['DELETE'])
def delete_status(id):
    status = Status.query.get_or_404(id)
    db.session.delete(status)
    db.session.commit()
    return '', 204
