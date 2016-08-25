from flask import Flask
import os

app = Flask(__name__, template_folder="../templates")
app.config.from_object(os.environ['APP_SETTINGS'])
from app import views
from app import models