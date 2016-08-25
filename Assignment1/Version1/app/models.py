from app import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class Input(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	person_name = db.Column(db.String(120))
	date_of_birth = db.Column(db.Date)
	timestamp = db.Column(db.DateTime)

	def __init__(self, person_name, date_of_birth):
		self.person_name = person_name
		self.date_of_birth = date_of_birth
		self.timestamp = datetime.datetime.utcnow()

	def __repr__(self):
		return "<Input {0}>".format(self.id)