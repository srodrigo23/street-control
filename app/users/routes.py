from flask import render_template
from app.users import bp

@bp.route('/')
def index():
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
  ]
  return render_template('users/index.html', data=data)
  # else:
  #   return redirect(url_for('main.show_the_login_form'))