from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    correo = EmailField("Correo electrónico", validators=[DataRequired()])
    contraseña = PasswordField("Contraseña", validators=[DataRequired()])
    entrar = SubmitField("Entrar")