from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import ContactoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "mi_clave_secreta_123"
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactoForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        correo = form.correo.data
        flash(f'¡Registro exitoso! Hola {nombre}', 'success')
        # ✅ Redirigimos a la página de confirmación
        return redirect(url_for('respuesta', nombre=nombre, correo=correo))
    return render_template('index.html', form=form)

@app.route('/respuesta/<nombre>/<correo>')
def respuesta(nombre, correo):
    return render_template('respuesta.html', nombre=nombre, correo=correo)

if __name__ == '__main__':
    app.run(debug=True)