from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    is_initial = db.Column(db.Boolean, default=False)

    transitions_from = db.relationship('Transition', backref='from_status', lazy=True, foreign_keys='Transition.from_status_id')
    transitions_to = db.relationship('Transition', backref='to_status', lazy=True, foreign_keys='Transition.to_status_id')

class Transition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    from_status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    to_status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
