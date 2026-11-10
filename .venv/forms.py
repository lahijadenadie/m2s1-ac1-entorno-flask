from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactoForm(FlaskForm):
    nombre = StringField(
        "Nombre",
        validators=[DataRequired(message="Escribe tu nombre")]
    )
    correo = StringField(
        "Correo",
        validators=[
            DataRequired(message="Escribe tu correo"),
            Email(message="Escribe un correo válido, por ejemplo ana@correo.com")
        ]
    )
    enviar = SubmitField("Enviar")