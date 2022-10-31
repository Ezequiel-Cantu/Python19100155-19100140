from serializer import Serializer
from app import db

class Obra(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    


class Museo(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))


class Artista(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))



class Escuela(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))



class Disciplina(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
