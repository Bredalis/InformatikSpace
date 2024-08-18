
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

# Conectar la bbdd 
cliente = MongoClient(os.getenv("CLAVE_MONGO"))
app.db = cliente["InformatikSpace"]
coleccion = app.db["Datos_Usuarios"]

# Rutas de la pagin

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Crear_Articulo", methods = ["GET", "POST"])
def crear_articulo():

    if request.method == "POST":

        contenido = [request.form.get("contenido")]
        contenido_dividido = [oracion.split("\r\n\r\n") for oracion in contenido]

        # Subir los datos a la bbdd
        coleccion.insert_one({"Contenido_Articulo": contenido_dividido})
        print("Se enviaron los datos! \U0001F642")

    return render_template("Crear_Articulo.html")

@app.route("/Mis_Articulos")
def mis_articulos():
    return render_template("Mis_Articulos.html")

@app.route("/Plantilla_Articulos")
def plantilla_articulos():
    return render_template("Plantilla_Articulos.html")

@app.route("/Buscador")
def buscador():
    return render_template("Buscador.html")

@app.route("/Seccion_Chatbots")
def seccion_chatbots():
    return render_template("Seccion_Chatbots.html")

@app.route("/Sobre_Nosotros")
def sobre_nosotros():
    return render_template("Sobre_Nosotros.html")

@app.route("/Login")
def login():
    return render_template("Inicio_Sesion.html")

@app.route("/404")
def error_404():
    return render_template("404.html")

if __name__ == "__main__":
    app.run()