from flask import render_template, url_for, redirect, flash
from blogger import app
from blogger.forms import LoginForm, RegistrationForm
from blogger.models import User, Post


posts = [
    {
        'author': 'Jason',
        'title': 'Blog Post #1',
        'content': ' I am so tired today...',
        'date_posted': 'August 17, 2055'
    },
    {
        'author': 'Valeria',
        'title': 'Blog Post #2',
        'content': ' Good morning!',
        'date_posted': 'August 18, 2055'       
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'milos@example.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check your data.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
