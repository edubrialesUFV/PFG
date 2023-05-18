from flask import Blueprint, render_template, redirect, url_for
from models import Usuario, Vm
from db import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from flask_login import login_required, current_user
from tasks import create_container
views = Blueprint("views", __name__)


class FormCreateVm(FlaskForm):
    nombre = StringField('Nombre de la maquina virtual', validators=[DataRequired()])
    so = SelectField('Sistema operativo de la maquina virtual', validators=[DataRequired()], choices=[('kali', 'Kali'), ('ubuntu', 'Ubuntu'), ('fedora', 'Fedora')])
    pers_datos = BooleanField('Perseverancia de datos')
    submit = SubmitField('Crear')
    
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/create_vm", methods=["GET", "POST"])
@login_required
def create_vm():
    form = FormCreateVm()
    if form.validate_on_submit():
        container_id = create_container.delay(form.so.data, current_user.nombre)
        new_vm = Vm(id = container_id, nombre = form.nombre.data ,so=form.so.data, pers_datos = form.pers_datos.data, usuario_id = current_user.id)
        db.session.add(new_vm)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("create_vm.html", form=form)