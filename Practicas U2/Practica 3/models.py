from app import db


class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    pais = db.Column(db.String(250))
    def __str__(self):
        return (f'Id: {self.id}, '
                f'Nombre: {self.nombre}, '
                f'Pais: {self.pais}, ')
        

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    genero = db.Column(db.String(250))
    def __str__(self):
        return (f'Id: {self.id}, '
                f'Nombre: {self.nombre}, '
                f'Genero: {self.genero}')

    


class Libreria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    lugar = db.Column(db.String(250))
    def __str__(self):
        return (f'Id: {self.id} , '
                f'Nombre: {self.nombre},' 
                f'Lugar: {self.lugar}')
    