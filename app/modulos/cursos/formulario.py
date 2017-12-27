# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    codigo = StringField('Código', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired()])
    #Telefono = StringField('Telefono', validators=[DataRequired()],render_kw={"placeholder": "Ingrese numero de 8 digitos"})
