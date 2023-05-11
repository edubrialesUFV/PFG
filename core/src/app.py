from flask import Flask
from flask_migrate import Migrate

from views import views
from config import DATABASE_URI
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(views)