from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import ContactoForm

# Inicializar app
app = Flask(__name__)
app.config['SECRET_KEY'] = "mi_clave_secreta_123"

# Configuración Base de Datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///proyecto.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cargar Bootstrap y Base de Datos
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# Modelo: Tabla Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)

# Crear la tabla en la base de datos
with app.app_context():
    db.create_all()

# Ruta principal (formulario)
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        correo = form.correo.data
        flash(f'¡Registro exitoso! Hola {nombre}', 'success')
        return redirect(url_for('respuesta', nombre=nombre, correo=correo))
    return render_template('index.html', form=form)

# Ruta de respuesta
@app.route('/respuesta/<nombre>/<correo>')
def respuesta(nombre, correo):
    return render_template('respuesta.html', nombre=nombre, correo=correo)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)