from flask import Flask, render_template, url_for
app = Flask(__name__)

# List of dictionary
posts = [
    {
        'author': 'Peter',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': '23-01-2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '24-01-2020'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'about')