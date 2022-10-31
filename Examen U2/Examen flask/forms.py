from flask import Flask
from models import Obra,Artista
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ObraForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    enviar = SubmitField("Aceptar")

class ArtistaForm(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    enviar = SubmitField("Aceptar")