from flask import render_template, url_for, redirect
from app.users import bp
from faker import Faker


fake = Faker()
data = [
  {
    "name" : "Sergio Rodrigo Cardenas Rivera",
    "user_name": "sergio.cardenas",
    "last_connection": "2023-03-29",
  },
  {
    "name" : "Miriam Lucana",
    "user_name": "miriam.lucana",
    "last_connection": "2023-03-29",
  },
  {
    "name" : "Pedro Peredo",
    "user_name": "pedro.peredo",
    "last_connection": "2023-03-29",
  },
  {
    "name" : "Jorge Javier",
    "user_name": "jorge.javier",
    "last_connection": "2023-03-29",
  },
]

@bp.route('/')
def index():
  return render_template('users/index.html', data=data)
  # else:
  #   return redirect(url_for('main.show_the_login_form'))
@bp.route('/add_user')
def method():
  new_data = {
    "name" : fake.name(),
    "user_name": fake.address(),
    "last_connection": "2023-03-29",
  }
  data.append(new_data)
  # return redirect(url_for('.index'))
  # return render_template('users/index.html', data=data)
  return new_data
  