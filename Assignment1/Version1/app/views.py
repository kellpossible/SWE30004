from app import app
from flask import request, flash
from flask import render_template
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from app.forms import AliveCalculatorForm
from app.models import Input, db


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/show/<id>/")
def show(id):
    iput = Input.query.get_or_404(id)
    return render_template("show.html", iput=iput)


@app.route("/new", methods=('GET', 'POST'))
def new():
    form = AliveCalculatorForm()
    if form.validate_on_submit():
        iput = Input(form.person_name.data, form.date_of_birth.data)
        db.session.add(iput)
        db.session.commit()
        return redirect("/show/{0}".format(iput.id))
    return render_template("new.html", form=form)


@app.route("/history")
def history():
    inputs = Input.query.all()
    return render_template("history.html", inputs=inputs)
