from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '93c6ce5477a92d7463f99239c2b9d7a5'
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

# bcrypt = Bcrypt(app)
database = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from fakepinterest import routes
