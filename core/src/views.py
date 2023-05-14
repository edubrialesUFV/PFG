from flask import Blueprint, render_template
from models import Usuario, Servicio, Usuario_Servicios
from db import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    servicios = Servicio.query.all()
    return render_template("index.html", servicios=servicios)


