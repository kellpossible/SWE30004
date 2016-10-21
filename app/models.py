from app import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)


class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(120))
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    date_of_birth = db.Column(db.Date)
    timestamp = db.Column(db.DateTime)

    def __init__(self, first_name, last_name, date_of_birth):
        self.person_name = None
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.timestamp = datetime.datetime.utcnow()

    def __repr__(self):
        return "<Input {0}>".format(self.id)

    def full_name(self):
        if self.person_name is None:
            return self.first_name + " " + self.last_name
        else:
            return self.person_name

    def calculate_earth_age_days(self):
        today = datetime.datetime.now()
        dob = datetime.datetime.combine(self.date_of_birth,
                                        datetime.datetime.min.time())
        diff = today - dob
        return diff.days
