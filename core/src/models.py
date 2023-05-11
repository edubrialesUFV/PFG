from db import db



class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    servicios = db.relationship('Usuario_Servicios', back_populates='usuario')

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