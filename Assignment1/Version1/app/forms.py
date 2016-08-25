from flask_wtf.form import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class AliveCalculatorForm(FlaskForm):
    person_name = StringField('Your Name', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d',
                              validators=[DataRequired()])
