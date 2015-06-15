from restau_management_flask import app, APP_STATIC
from flask import render_template, redirect, url_for
from .models import Restaurant
import os


restau_name = app.config["RESTAU_NAME"]
table_nb = app.config["TABLE_NB"]
r = Restaurant(restau_name, table_nb)
menu_file = os.path.join(APP_STATIC, "menu.txt")
r.load_menu(menu_file=menu_file)
print(len(r.menu.dishes))


@app.route("/")
def index():
  return render_template("index.html", r = r)

@app.route("/menu")
def menu():
  return render_template("menu.html", menu=r.menu)

@app.route("/refresh-menu")
def refresh_menu():
  r.load_menu(menu_file = menu_file)
  return redirect(url_for("menu"))

