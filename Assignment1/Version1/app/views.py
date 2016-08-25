from app import app
from flask import request
from flask import render_template
from flask import url_for, redirect
from flask_sqlalchemy import SQLAlchemy


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/alive_calculator")
def alive_calculator():
    return render_template("alive_calculator.html")

@app.route("/history")
def history():
	return render_template("history.html")