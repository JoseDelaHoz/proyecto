
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app

db = SQLAlchemy(app)

models = {}  

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False)
    rut = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True ,nullable=False)
    telefono = db.Column(db.Text, nullable=False)
    contrasena = db.Column(db.Text, nullable=False)
    rol = db.Column(db.Integer, nullable=False)
    secciones = db.relationship('Secciones')


class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    codigo = db.Column(db.Text, nullable=False)
    secciones = db.relationship('Secciones')
    

class Secciones(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     usuario_id = db.Column(db.Integer,  db.ForeignKey(Usuarios.id),nullable=False)
     curso_id = db.Column(db.Integer, db.ForeignKey(Cursos.id), nullable=False)
     numero = db.Column(db.Integer, nullable=False)
     ano = db.Column(db.Integer, nullable=False)
     semestre = db.Column(db.Integer, nullable=False)
     horario = db.Column(db.Text, nullable=False)
     usuario = db.relationship('Usuarios')
     curso = db.relationship('Cursos')
     comentarios = db.relationship('Comentarios')
    

class Ayudantes(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(30), nullable=False)
     apellido = db.Column(db.String(30), nullable=False)
     comentarios = db.relationship('Comentarios')
    

class Comentarios(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     ayudante_id = db.Column(db.Integer,  db.ForeignKey(Secciones.id),nullable=False)
     seccion_id = db.Column(db.Integer, db.ForeignKey(Ayudantes.id), nullable=False)
     comentario = db.Column(db.Text, nullable=False)
     estrella = db.Column(db.Integer, nullable=False)
     seccion = db.relationship('Secciones')
     ayudante = db.relationship('Ayudantes')


models['ayudantes'] = Ayudantes
models['cursos'] = Cursos
models['comentarios'] = Comentarios
models['usuarios'] = Usuarios
models['secciones'] = Secciones


#db.drop_all()
#db.create_all()
