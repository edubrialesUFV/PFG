from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from views import views
from users import users
from config import DATABASE_URI
from db import db
from models import Usuario

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(views)
app.register_blueprint(users)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))