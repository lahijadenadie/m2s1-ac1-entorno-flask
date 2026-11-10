from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_practica'

# Ruta raíz redirige al login
@app.route('/')
def inicio():
    return redirect(url_for('login'))

# Ruta del formulario de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "✅ Inicio de sesión correcto"
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)