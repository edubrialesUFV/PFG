from flask_sqlalchemy import SQLAlchemy
from celery import Celery

db = SQLAlchemy()
celery = Celery()

#Migraciones en la base de datos:
#- flask db migrate -m "primera migracion"
#- flask db upgrade