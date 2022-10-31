from flask import Flask, request,jsonify ,url_for, render_template, redirect, session
from database import db
from flask_migrate import Migrate
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from models import Obra,Museo,Escuela,Artista,Disciplina
from forms import ObraForm,ArtistaForm

app = Flask(__name__)

USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'flask_examen'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACE_MODIFICATION'] = False

app.config['SECRET_KEY'] = 'malditocarlos'


db.init_app(app)


migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/artista')
def artistas():
    if 'username' in session:
        artistas = Artista.query.all()
        return render_template('/artista/artistas.html',artistas = artistas)
    else:
        return redirect(url_for('login'))

@app.route('/artistas/<int:id>')
def verartista(id):
    if 'username' in session:
        artista = Artista.query.get_or_404(id)
        return render_template('/artista/detalleartista.html',artista = artista)
    else:
        return redirect(url_for('login'))

@app.route('/artistas/agregar', methods=["GET","POST"])
def agregarartista():
    if 'username' in session:
        artista = Artista()
        artistaForm = ArtistaForm(obj=artista)
        if request.method == "POST":
            if artistaForm.validate_on_submit():
                artistaForm.populate_obj(artista)
                db.session.add(artista)
                db.session.commit()
                return redirect(url_for("artistas"))
        return render_template('/artista/agregarartista.html', forma = artistaForm)
    else:
        return redirect(url_for('login'))

@app.route('/artistas/editar/<int:id>', methods=["GET","POST"])
def editarartista(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        artista = Artista.query.get_or_404(id)
        artistaForm = ArtistaForm(obj=artista)
        if request.method == "POST":
            if artistaForm.validate_on_submit():
                artistaForm.populate_obj(artista)
                db.session.commit()
                return redirect(url_for("artistas"))
        return render_template('/artista/editarartista.html', forma = artistaForm)
    else:
        return redirect(url_for('login'))


@app.route('/artistas/eliminar/<int:id>')
def eliminarartista(id):
    if 'username' in session:
        app.logger.debug(request.headers.get('token'))
        artista = Artista.query.get_or_404(id)
        db.session.delete(artista)
        db.session.commit()
        return redirect(url_for('artistas'))
    else:
        return redirect(url_for('login'))

