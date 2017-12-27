# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Required
from wtforms.validators import Length, Email


class Formulario(FlaskForm):
    name = StringField('Nombre', validators=[Required()])
    lastname = StringField('Apellido', validators=[DataRequired()])
    rut = StringField('Rut', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    telefono = StringField('Teléfono (+56 9)', validators=[DataRequired()],render_kw={"placeholder": "Ingrese número de 8 dígitos"})
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    rol = SelectField('Rol', validators=[DataRequired()], choices = [('admin', 'Administrador'), ('user', 'Profesor')])