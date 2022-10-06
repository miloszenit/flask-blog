from flask import Blueprint

bp = Blueprint('users', __name__)

from blogger.users import routes
