from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired

class Formulario(FlaskForm):
    # name = StringField('Nombre', validators=[DataRequired()])
    # lastname = StringField('Apellido', validators=[DataRequired()])
    # rut = StringField('Rut', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired()])
    # telefono = StringField('Telefono (+56 9)', validators=[DataRequired()],render_kw={"placeholder": "Ingrese numero de 8 digitos"})
    # contrasena = PasswordField('Clave', validators=[DataRequired()])
    # rol = SelectField('Rol', validators=[DataRequired()], choices = [('admin', 'Profesor'), ('user', 'Ayudante')])