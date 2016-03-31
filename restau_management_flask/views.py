from restau_management_flask import app, APP_STATIC
from flask import render_template, redirect, url_for, flash
from .models import Restaurant
import os
from .forms import AddGroupForm, ReleaseGroupTable, OrderDishesForm


restau_name = app.config["RESTAU_NAME"]
table_nb = app.config["TABLE_NB"]
r = Restaurant(restau_name, table_nb)
menu_file = os.path.join(APP_STATIC, "menu.txt")
r.load_menu(menu_file=menu_file)


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

@app.route("/groups", methods=['GET', 'POST'])
def add_group():
  form = AddGroupForm()
  form2 =ReleaseGroupTable()
  form3 = OrderDishesForm()
  if form.validate_on_submit():
    customer_nb = form.customer_nb.data
    table_nb = r.new_customer_group(customer_nb)
    if table_nb is None:
      flash('Sorry, no available tables at the moment.')
    else:
      flash('Table {} are available for this customer group.'.format(', '.join(map(str, table_nb))))
  return render_template("groups.html", form=form, form2=form2, form3=form3, customer_groups=r.customer_groups, free_tables=r.free_tables,)

@app.route("/release-table", methods=['POST'])
def release_table():
  form = AddGroupForm()
  form2 =ReleaseGroupTable()
  form3 = OrderDishesForm()
  if form2.validate_on_submit():
    customer_id = form2.customer_id.data
    group_leaving = None
    for group in r.customer_groups:
      if int(customer_id) == group.id:
        group_leaving = group
        break
    if group_leaving is None:
      flash("No leaving group found.")
    else:
      r.customer_group_leave(group_leaving)
      flash("Group {} removed.".format(customer_id))
    return render_template("groups.html", form=form, form2=form2, form3=form3, customer_groups=r.customer_groups, free_tables=r.free_tables)

@app.route("/release-table-v2/<int:id>")
def release_table_v2(id):
  form = AddGroupForm()
  form2 = ReleaseGroupTable()
  form3 = OrderDishesForm()
  group_leaving = None
  for group in r.customer_groups:
    if id == group.id:
      group_leaving = group
      break
  if group_leaving is None:
    flash("No leaving group found.")
  else:
    r.customer_group_leave(group_leaving)
    flash("Group {} removed.".format(id))
  return render_template("groups.html", form=form, form2=form2, form3=form3, customer_groups=r.customer_groups, free_tables=r.free_tables)

@app.route("/order-dishes", methods=['POST'])
def order_dishes():
  form = AddGroupForm()
  form2 = ReleaseGroupTable()
  form3 = OrderDishesForm()
  if form3.validate_on_submit():

    dish_nb = form3.dish_nb.data
    customer_id = form3.customer_id.data

    current_dishes = []
    for dish in r.menu.dishes:
        if int(dish.number) == int(dish_nb):
            current_dishes.append(dish)
            break

    current_group = None
    for group in r.customer_groups:
        if int(group.id) == int(customer_id):
            # current_group = group
            group.order_dishes(current_dishes)
            break

    if current_group is None:
        flash("Group not exists.")


    return render_template("groups.html", form=form, form2=form2, form3=form3, customer_groups=r.customer_groups, free_tables=r.free_tables)
