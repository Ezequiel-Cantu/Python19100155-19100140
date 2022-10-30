from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LibroForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    genero = StringField('genero')
    enviar = SubmitField('enviar')


class LibreriaForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    lugar = StringField('lugar')
    enviar = SubmitField('enviar')


class AutorForm(FlaskForm):
    nombre = StringField('nombre', validators=[DataRequired()])
    pais = StringField('pais')
    enviar = SubmitField('enviar')
