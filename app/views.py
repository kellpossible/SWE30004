from app import app
from flask import request, flash
from flask import render_template
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app.forms import AliveCalculatorForm
from app.models import Input, db
from flask.ext.navigation import Navigation

nav = Navigation(app)
nav.Bar('top',
        [
          nav.Item('Home', 'index'),
          nav.Item('New Calculation', 'new'),
          nav.Item('History', 'history')
        ])

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/show/<int:id>/")
def show(id):
    iput = Input.query.get_or_404(id)
    return render_template("show.html", iput=iput)


@app.route("/new", methods=('GET', 'POST'))
def new():
    form = AliveCalculatorForm()
    if form.validate_on_submit():
        iput = Input(form.first_name.data, form.last_name.data, form.date_of_birth.data)
        db.session.add(iput)
        db.session.commit()
        return redirect("/show/{0}".format(iput.id))
    return render_template("new.html", form=form)


@app.route("/history")
def history():
    inputs = Input.query.all()
    return render_template("history.html", inputs=inputs)
