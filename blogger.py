from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
