from blogger.main import bp
from flask import render_template, request
from blogger.models import Post


@bp.route("/")
@bp.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', posts=posts)


@bp.route("/about")
def about():
    return render_template('about.html', title='About')
