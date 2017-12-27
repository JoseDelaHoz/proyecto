# -*- coding: utf8 -*-
from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from formulario import Formulario
from app.login import requires_auth
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask
import sqlite3


module = Blueprint('comentarios', __name__, template_folder='templates')

@module.route('/crear', methods=['GET', 'POST'])
@requires_auth
def crear():
	form = Formulario()

	ayudantes = [(ayudante.id,"%s %s"%(ayudante.nombre,ayudante.apellido)) for ayudante in  module.models['ayudantes'].query.all()]
	# print ayudantes

	secciones = [(seccion.id,"%s %s %s %s"%(seccion.numero,seccion.ano,seccion.semestre,seccion.horario)) for seccion in  module.models['secciones'].query.all()]
	# print secciones

	creado = False
	if request.method == 'POST':
		form = Formulario(request.form)

		comentario = module.models['comentarios']()
		comentario.ayudante_id = form.ayudante.data
		comentario.seccion_id = form.seccion.data
	 	comentario.estrella = form.estrella.data
		comentario.comentario = form.comentario.data


		module.db.session.add(comentario)
		module.db.session.commit()
		creado = True

	form.ayudante.choices = ayudantes
	form.seccion.choices = secciones

	return render_template("comentarios_index.html", form=form, creado=creado)



@module.route('/buscar', methods=['GET', 'POST'])
@requires_auth
def buscar():

	sql ="""SELECT 
usuarios.nombre,
usuarios.apellido,
ayudantes.nombre,
ayudantes.apellido,
cursos.nombre AS nombre_curso,
cursos.codigo,
secciones.numero AS numero_seccion,
secciones.ano AS año,
secciones.semestre,
secciones.horario,
comentarios.estrella,
comentarios.comentario
FROM
usuarios,
ayudantes,
cursos,
secciones,
comentarios
where 
usuarios.id = comentarios.estrella and
ayudantes.id = comentarios.ayudante_id and
comentarios.seccion_id = secciones.id and
secciones.curso_id = cursos.id
ORDER BY ayudantes.nombre ASC"""

	
	return render_template("comentarios_tables.html",resultados = module.db.engine.execute(sql))	