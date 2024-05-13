from flask import Flask, url_for, send_from_directory
from app.extensions import db
from app.extensions import migrate
from config import config

import os

from app.models import person, session, user_credentials

# from app.queries import person


def create_app():
    
    app = Flask(__name__)
    app.config.from_object(config[os.environ.get("CONFIG_MODE")])
    
    # Initialize Flask extensions here

    with app.app_context():
        db.init_app(app)
        db.create_all()

        migrate.init_app(app, db)
        
        #Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(blueprint=main_bp)
    
    from app.users import bp as users_bp
    app.register_blueprint(blueprint=users_bp, url_prefix="/users")

    from app.meetings import bp as meetings_bp
    app.register_blueprint(blueprint=meetings_bp, url_prefix="/meetings")

    from app.attendance import bp as attendance_bp
    app.register_blueprint(blueprint=attendance_bp, url_prefix="/attendance")
    
    from app.collections import bp as collection_bp
    app.register_blueprint(blueprint=collection_bp, url_prefix="/collections")
        
        # @app.route('/favicon.ico')
        # def favicon():
        #     return send_from_directory(
        #         directory=os.path.join(app.root_path, 'static'),
        #         path='static/favicon.ico', 
        #         mimetype='image/vnd.microsoft.icon'
        #     )

        # @app.route('/test/')
        # def test_page():
        #   return '<h1>Testing the Flask Application Factory Pattern</h1>'
        
    return app
