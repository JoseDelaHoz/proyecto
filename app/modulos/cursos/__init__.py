# -*- coding: utf8 -*-
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from formulario import Formulario

from app.login import requires_auth

module = Blueprint('cursos', __name__,
                        template_folder='templates')

@module.route('/crear', methods=['GET', 'POST'])
@requires_auth
def crear():
	form = Formulario()

	creado = False
	if request.method == 'POST':
		form = Formulario(request.form)

		curso =  module.models['cursos']()
		curso.nombre = form.name.data
		curso.codigo = form.codigo.data

		module.db.session.add(curso)
		module.db.session.commit()
		creado = True

	return render_template("cursos_index.html", form=form,creado=creado)
