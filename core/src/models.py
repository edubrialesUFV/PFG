from db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Enum

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    vm = db.relationship('Vm', backref='usuario')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Vm(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pers_datos = db.Column(db.Boolean, default = False)
    so = db.Column(Enum('Kali', 'Ubuntu', 'Fedora', name='so'), nullable=False)
    port = db.Column(db.Integer, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

