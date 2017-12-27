# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField,HiddenField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    ayudante = SelectField('Seleccione Ayudante', validators=[DataRequired()], choices=[])
    seccion = SelectField('Seleccione Sección', validators=[DataRequired()], choices=[])
    # nota = SelectField('Seleccione Nota', validators=[DataRequired()], choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    comentario = TextAreaField('Ingrese un comentario', validators=[DataRequired()])
    estrella = HiddenField()