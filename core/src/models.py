from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    servicios = db.relationship('Usuario_Servicios', back_populates='usuario')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuarios = db.relationship('Usuario_Servicios', back_populates='servicio')


class Usuario_Servicios(db.Model):
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('servicio.id'), primary_key=True)
    caracteristica1 = db.Column(db.String(100))
    caracteristica2 = db.Column(db.String(100))

    usuario = db.relationship(Usuario, back_populates="servicios")
    servicio = db.relationship(Servicio, back_populates="usuarios")



