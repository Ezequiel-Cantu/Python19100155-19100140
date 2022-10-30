import json
import re
from flask import Flask,request,url_for,render_template,redirect,jsonify
from database import db
from flask_migrate import Migrate
from forms import LibreriaForm,LibroForm,AutorForm
from models import Autor,Libreria,Libro

app = Flask(__name__)

#config

USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'prac3_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db.init_app(app)


migrate = Migrate()
migrate.init_app(app,db)

app.config["SECRET_KEY"] = "llave"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    libros = Libro.query.all()
    librerias = Libreria.query.all()
    autores=Autor.query.all()
    return render_template('index.html',libros=libros,autores=autores)


@app.route('/agregarautor', methods=['GET','POST'])
def agregarautor():
    autor = Autor()
    autorForm = AutorForm(obj=autor)
    if request.method == "POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            #insert
            db.session.add(autor)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarautor.html',forma=autorForm)

@app.route('/agregarlibro', methods=['GET','POST'])
def agregarlibro():
    libro = Libro()
    libroForm = LibroForm(obj=libro)
    if request.method == "POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            #insert
            db.session.add(libro)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarlibro.html',forma=libroForm)

@app.route('/libreria', methods=['POST','GET','PATCH','DELETE'])
def libreria():
    info = request.json
    libreria = Libreria()
    libreria.id = info["id"]
    libreria.nombre = info["nombre"]
    libreria.lugar = info["lugar"]
    
    if request.method == "POST":
            #insert
        res = db.session.add(libreria)
        db.session.commit()
        return jsonify(res)
    if request.method == "GET":
       return jsonify(info)
    if request.method == "PATCH":
        libreria.verified = True
        db.session.commit()
        return jsonify(res)
    return jsonify(libreria)

@app.route('/editarautor/<int:id>',methods=['GET','POST'])
def editarautor(id):
    autor = Autor.query.get_or_404(id)
    autorForm = AutorForm(obj=autor)
    if request.method=="POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarautor.html', forma=autorForm)

@app.route('/editarlibro/<int:id>',methods=['GET','POST'])
def editarlibro(id):
    libro = Libro.query.get_or_404(id)
    libroForm = LibroForm(obj=libro)
    if request.method=="POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarlibro.html', forma=libroForm)

@app.route('/eliminarautor/<int:id>')
def eliminarautor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarlibro/<int:id>')
def eliminarlibro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/verlibro/<int:id>')
def verDetalleLibro(id):
    libro = Libro.query.get_or_404(id)
    return render_template('detallelibro.html',libro=libro)
@app.route('/verautor/<int:id>')
def verDetalleAutor(id):
    autor = Autor.query.get_or_404(id)
    return render_template('detalleautor.html',autor=autor)