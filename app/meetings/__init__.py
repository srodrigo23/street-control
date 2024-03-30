from flask import Blueprint

bp = Blueprint('meetings', __name__)

from app.meetings import routes