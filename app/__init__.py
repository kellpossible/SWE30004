from flask import Flask
import os
import sys

app = Flask(__name__)
try:
	print("SERVER_NAME:" + os.environ['SERVER_NAME'])
	print("PORT:" + int(os.environ.get("PORT",80)))
	app.config.from_object(os.environ['APP_SETTINGS'])
except KeyError:
	print("Please set APP_SETTINGS in your environment. e.g. export APP_SETTINGS=config.DevelopmentConfig")
	sys.exit()


from app import views
from app import models