from restau_management_flask import app
from flask import render_template
from .models import Restaurant

restau_name = app.config["RESTAU_NAME"]
table_nb = app.config["TABLE_NB"]
r = Restaurant(restau_name, table_nb)

@app.route("/")
def index():
  return render_template("index.html", r = r)
