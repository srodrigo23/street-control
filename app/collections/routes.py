from flask import render_template
from app.collections import bp

@bp.route('/')
def index():
  data = {
      "name": "Sergio Rodrigo Cárdenas Rivera",
      "ci": "5555555",
      "debts":[
        {
          "id": "1",
          "date": "12/12/2023",
          "reason": 1,
          "detail": "cargo por agua del mes de agosto",
          "amount": 123,
        },
        {
          "id": "2",
          "date": "12/12/2023",
          "reason": 1,
          "detail": "cargo por agua del mes de agosto",
          "amount": 123,
        },
        {
          "id": "3",
          "date": "12/12/2023",
          "reason": 1,
          "detail": "cargo por agua del mes de agosto",
          "amount": 123,
        }
      ]
    }
  
  return render_template('collections/index.html', data=data)
  # else:
  #   return redirect(url_for('main.show_the_login_form'))