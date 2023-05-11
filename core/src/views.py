from flask import Blueprint, render_template
from models import Usuario, Servicio, Usuario_Servicios
from db import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    servicios = Servicio.query.all()
    # nuevo_servicio = Services("pepe")
    # db.session.add(nuevo_servicio)
    # db.session.commit()
    return render_template("base.html", servicios=servicios)
