# -*- coding: utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    usuario = SelectField('Seleccione Usuario', validators=[DataRequired()], choices=[])
    cursos = SelectField('Seleccione Curso', validators=[DataRequired()], choices=[])
    numero = StringField('Número de Sección', validators=[DataRequired()])
    ano = SelectField('Año', validators=[DataRequired()], choices=[('2017','2017'), ('2018','2018')])
    semestre = SelectField('Semestre', choices=[('Otoño','Otoño'), ('Primavera','Primavera')])
    horario = SelectField('Horario', validators=[DataRequired()], choices=[('A','8:30 - 9:50 Bloque A'), ('B','10:00 - 11:20 Bloque B'), ('C','11:30 - 12:50 Bloque C'), ('D','14:00 - 15:20 Bloque D'), ('E','15:30 - 16:50 Bloque E'), ('F','17:00 - 18:20 Bloque F')])
    
