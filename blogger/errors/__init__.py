from flask import Blueprint

bp = Blueprint('errors', __name__)

from blogger.errors import handlers
