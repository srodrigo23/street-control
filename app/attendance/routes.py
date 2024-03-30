from flask import render_template
from app.attendance import bp

@bp.route('/')
def index():
  data = [
    {
      "creation_date" : "2023-03-29",
      "scheduled_date" : "2023-04-23",
      "creator_user_name": "sergio.cardenas",
      "description": "Se invita a todos los vecinos a la realizacion del pago del agua",
    },
  ]
  return render_template('attendance/index.html', data=data)
  # else:
  #   return redirect(url_for('main.show_the_login_form'))