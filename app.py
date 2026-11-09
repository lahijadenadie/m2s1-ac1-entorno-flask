import os
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

# PRIMERO creamos la app (MUY IMPORTANTE que vaya aquí)
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


# Ruta Inicio
@app.route("/")
def index():
    return render_template("index.html")


# Ruta About (DESPUÉS de crear "app")
@app.route("/about")
def about():
    return render_template("about.html", proyecto="Mi primer app Flask")


if __name__ == "__main__":
    app.run(debug=True)
