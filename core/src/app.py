from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from views import views
from users import users
from config import DATABASE_URI
from db import db, celery
from models import Usuario
import os
from dotenv import load_dotenv
import tasks
load_dotenv()


def make_celery(app):
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = Flask(__name__)
app.register_blueprint(views)
app.register_blueprint(users)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['CELERY_BROKER_URL'] = os.environ.get('CELERY_BROKER_URL')
app.config['CELERY_RESULT_BACKEND'] = os.environ.get('CELERY_RESULT_BACKEND')
celery = make_celery(app)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

migrate = Migrate(app, db)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

