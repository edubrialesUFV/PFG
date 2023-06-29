from flask import Blueprint, render_template, redirect, url_for
from models import Usuario, Vm, Code
from db import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from flask_login import login_required, current_user
from tasks import create_container, delete_container, create_container_ui, create_container_code
views = Blueprint("views", __name__)


class FormCreateVm(FlaskForm):
    nombre = StringField('Nombre de la maquina virtual', validators=[DataRequired()])
    so = SelectField('Sistema operativo de la maquina virtual', validators=[DataRequired()], choices=[('kali', 'Kali'), ('ubuntu', 'Ubuntu')])
    pers_datos = BooleanField('Perseverancia de datos')
    submit = SubmitField('Crear maquina')


class FormCreateUi(FlaskForm):
    nombre_ui = StringField('Nombre de la maquina virtual', validators=[DataRequired()])
    so_ui = SelectField('Sistema operativo de la maquina virtual', validators=[DataRequired()], choices=[ ('ubuntu', 'Ubuntu'), ('fedora', 'Fedora')])
    pers_datos_ui = BooleanField('Perseverancia de datos')
    submit_ui = SubmitField('Crear maquina')

class FormCreateCode(FlaskForm):
    nombre_code = StringField('Nombre del codespace', validators=[DataRequired()])
    lenguaje = SelectField('Lenguaje de programación', validators=[DataRequired()], choices=[ ('python', 'Python'), ('python', 'C'), ('java', 'Java')])
    submit_code = SubmitField('Crear codespace')

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    maquinas = current_user.vm
    codespaces = current_user.code
    form = FormCreateVm()
    form1 = FormCreateUi()
    form2 = FormCreateCode()

    if form.validate_on_submit():
        num = Vm.query.count()
        task = create_container.delay(form.nombre.data.replace(" ", ""), form.so.data, current_user.nombre)
        container_id = task.get() 
        new_vm = Vm(id = container_id, nombre = form.nombre.data ,so=form.so.data, pers_datos = form.pers_datos.data, usuario_id = current_user.id)
        db.session.add(new_vm)
        db.session.commit()
        return redirect(url_for('views.home'))

    if form1.validate_on_submit():
        task = create_container_ui.delay(form1.nombre_ui.data.replace(" ", ""), form1.so_ui.data, current_user.nombre)
        container_id = task.get() 
        new_vm = Vm(id = container_id, nombre = form1.nombre_ui.data ,so=form1.so_ui.data, pers_datos = form1.pers_datos_ui.data, ui=True,  usuario_id = current_user.id)
        db.session.add(new_vm)
        db.session.commit()
        return redirect(url_for('views.home'))
    
    if form2.validate_on_submit():
        task = create_container_code.delay(form2.nombre_code.data.replace(" ", ""), form2.lenguaje.data, current_user.nombre)
        container_id = task.get() 
        new_code = Code(id = container_id, nombre = form2.nombre_code.data ,leng=form2.lenguaje.data, usuario_id = current_user.id)
        db.session.add(new_code)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("index.html", maquinas=maquinas, form=form, form1=form1, form2=form2, codespaces=codespaces)

# @views.route("/create_vm", methods=["GET", "POST"])
# @login_required
# def create_vm():
#     form = FormCreateVm()
#     if form.validate_on_submit():
#         num = Vm.query.count()
#         task = create_container.delay(form.nombre.data, form.so.data, current_user.nombre, 7681+num)
#         container_id = task.get() 
#         new_vm = Vm(id = container_id, nombre = form.nombre.data ,so=form.so.data, pers_datos = form.pers_datos.data, port=7681+num, usuario_id = current_user.id)
#         db.session.add(new_vm)
#         db.session.commit()
#         return redirect(url_for('views.home'))
#     return render_template("create_vm.html", form=form)



@views.route("/start/vm/<string:container>")
@login_required
def start_container(container):
    container = Vm.query.get_or_404(container)
    user = current_user.nombre
    return redirect(f"http://{container.nombre}.{user}.localhost")


@views.route("/delete/vm/<string:container>")
@login_required
def eliminar_container(container):
    container = Vm.query.get_or_404(container)
    db.session.delete(container)
    db.session.commit()
    delete_container(container.id)
    return redirect(url_for('views.home'))


@views.route("/start/code/<string:container>")
@login_required
def start_container_code(container):
    container = Code.query.get_or_404(container)
    user = current_user.nombre
    return redirect(f"http://{container.nombre}.{user}.localhost")

@views.route("/delete/code/<string:container>")
@login_required
def eliminar_container_code(container):
    container = Code.query.get_or_404(container)
    db.session.delete(container)
    db.session.commit()
    delete_container(container.id)
    return redirect(url_for('views.home'))