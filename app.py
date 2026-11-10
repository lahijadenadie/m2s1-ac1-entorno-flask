from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import ContactoForm

# PRIMERO se crea la variable app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_para_pruebas'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Modelo Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

# Ruta principal con la lista de mascotas (Práctica 6)
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactoForm()
    mascotas = [
        {"nombre": "Luna", "tipo": "Perro"},
        {"nombre": "Milo", "tipo": "Gato"},
        {"nombre": "Nemo", "tipo": "Pez"}
    ]
    if form.validate_on_submit():
        nuevo_usuario = Usuario(nombre=form.nombre.data, correo=form.correo.data)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, mascotas=mascotas)

# Ruta Acerca
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)