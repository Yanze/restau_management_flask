from flask import Flask
import os # operating system

app = Flask(__name__)
app.config.from_object('config')
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # to get the root of the web app(a string with app root folder)
APP_STATIC = os.path.join(APP_ROOT, "static") # get the location of the static folder

from restau_management_flask import views






