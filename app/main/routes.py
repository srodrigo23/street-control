from flask import render_template, current_app, send_from_directory, send_file, redirect, url_for
from flask import session
from flask import request
from app.main import bp

# import os

@bp.route('/')
def index():
  if 'username' in session:
    # messages = request.args['messages']
    if 'is_admin' in session:
      return render_template('index.html', is_admin=True)
    else:
      return render_template('index.html')
  else:
    return redirect(url_for('main.show_the_login_form'))

# @bp.route('/login', methods=['GET', 'POST'])
# def login():
#   if request.method == 'POST':
#     return do_the_login()
#   else:
#     return show_the_login_form()

@bp.get('/login')
def show_the_login_form():
  return render_template('login.html')

@bp.post('/login')
def do_the_login():
  if request.method == "POST":
    data = request.get_json()
    username = data['username']
    password = data['password']
    # username = request.form.get("username")
    # password = request.form.get("password")
    if username == "admin" and password == "admin":
      session['username'] = username
      session['is_admin'] = True

      return {'status': 'success'}#username, password
      # return redirect(url_for('main.index'))
      # return redirect(url_for('.index'))
    else:
      return '<h1>wrong</h1>'
      # return render_template('login.html', error=True)

@bp.route('/logout')
def log_out():
  # clear session
  session.pop('username', None)
  return redirect(url_for('main.show_the_login_form'))

# @bp.route('/qrgenerator')
# def qr_generator()->None:
#     text_for_qr = "this is a text for qr code"
#     img = qrcode.make(text_for_qr)
#     img.save("app/qr_generated/qrcode1.png")
#     return '<h1>qr generated</h1>'

# @bp.route('/uploads/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     # Appending app path to upload folder path within app root folder
#     folder='static'
#     uploads = os.path.join(
#         current_app.root_path,
#         folder,
#         'qr_generated'
#         # app.config['UPLOAD_FOLDER']
#     )
#     # print(uploads)
#     # filename_to_download = filename[0:filename.find(' '):]
#     # print(filename_to_download)
#     # Returning file from appended path
#     # return send_from_directory(directory=uploads,path=filename)
#     return send_file(download_name=filename, path_or_file=uploads+'/'+filename, as_attachment=True)
#     # return render_template('index.html')