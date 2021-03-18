from flask import Flask, render_template, url_for
from forms import SignUpForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '110e87edbf8ccf68056f4fdd2b33aeb1'

posts = [
    {
        'author': 'Omar Lopez',
        'title': 'First Post',
        'content': 'Hi, my name is Omar Lopez',
        'date_posted': 'March 18, 2021'
    },
    {
        'author': 'Lebron James',
        'title': 'Second Post',
        'content': 'Hi, my name is Lebron James',
        'date_posted': 'March 19, 2021'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)