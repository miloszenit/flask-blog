from flask import Blueprint

bp = Blueprint('posts', __name__)

from blogger.posts import routes
