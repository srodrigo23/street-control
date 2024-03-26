from flask import render_template
from app.users import bp

@bp.route('/')
def index():
  return render_template('users/index.html')
  # else:
  #   return redirect(url_for('main.show_the_login_form'))