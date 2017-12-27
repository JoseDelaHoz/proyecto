# -*- coding: utf8 -*-
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from formulario import Formulario

from app.login import requires_auth

module = Blueprint('secciones', __name__, template_folder='templates')

@module.route('/crear', methods=['GET', 'POST'])
@requires_auth
def crear():
	

	usuarios = [(usuario.id,"%s %s"%(usuario.nombre,usuario.apellido)) for usuario in  module.models['usuarios'].query.all()]
	# print usuarios

	cursos = [(curso.id,"%s %s"%(curso.nombre,curso.codigo)) for curso in  module.models['cursos'].query.all()]
	# print cursos	


	creado = False
	if request.method == 'POST':
		form = Formulario(request.form)

		seccion =  module.models['secciones']()
		seccion.ano = form.ano.data
		seccion.semestre = form.semestre.data
		seccion.usuario_id = form.usuario.data
		seccion.curso_id = form.cursos.data
		seccion.numero = form.numero.data
		seccion.ano = form.ano.data
		seccion.semestre = form.semestre.data
		seccion.horario = form.horario.data
		module.db.session.add(seccion)
		module.db.session.commit()
		creado = True

	form = Formulario()

	form.usuario.choices=usuarios
	form.cursos.choices=cursos	

	return render_template("secciones_index.html", form=form, creado=creado)
