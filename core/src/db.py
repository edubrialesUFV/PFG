from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#Migraciones en la base de datos:
#- flask db migrate -m "primera migracion"
#- flask db upgrade