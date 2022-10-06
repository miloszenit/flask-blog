from flask import Blueprint

bp = Blueprint('main', __name__)

from blogger.main import routes
