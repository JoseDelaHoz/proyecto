# -*- coding: utf8 -*-
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from formulario import Formulario

from app.login import requires_auth

module = Blueprint('ayudantes', __name__,
                        template_folder='templates')

@module.route('/crear', methods=['GET', 'POST'])
@requires_auth
def crear():
	form = Formulario()

	creado = False
	if request.method == 'POST':
		form = Formulario(request.form)

		ayudante =  module.models['ayudantes']()
		ayudante.nombre = form.name.data
		ayudante.apellido = form.lastname.data

		module.db.session.add(ayudante)
		module.db.session.commit()
		creado = True

	return render_template("ayudantes_index.html", form=form,creado=creado)