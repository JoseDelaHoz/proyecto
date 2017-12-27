# -*- coding: utf8 -*-
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from formulario import Formulario

from app.login import requires_auth

module = Blueprint('usuarios', __name__, template_folder='templates')

@module.route('/crear', methods=['GET', 'POST'])
@requires_auth
def crear():
	form = Formulario()

	creado = False
	if request.method == 'POST':
		form = Formulario(request.form)

		usuario =  module.models['usuarios']()
		usuario.nombre = form.name.data
		usuario.apellido = form.lastname.data
		usuario.rut = form.rut.data
		usuario.email = form.email.data
		usuario.telefono = form.telefono.data
		usuario.contrasena = form.contrasena.data
		usuario.rol = form.rol.data

		module.db.session.add(usuario)
		module.db.session.commit()
		creado = True

	return render_template("usuarios_index.html", form=form, creado=creado)