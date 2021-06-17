from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '110e87edbf8ccf68056f4fdd2b33aeb1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# importing blueprints routes
from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main

# registering blueprints
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)