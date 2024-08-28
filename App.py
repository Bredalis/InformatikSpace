
from flask import Flask, render_template, request, abort, redirect, url_for, session
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

def informatikspace():

    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    # Conectar la bbdd 
    cliente = MongoClient(os.getenv("CLAVE_MONGO"))
    app.db = cliente["InformatikSpace"]
    coleccion_articulo = app.db["Datos_Articulos"]
    coleccion_usuario = app.db["Datos_Usuarios"]

    # Obtener los contenidos y temas de los artículos
    articulos = [
        {
            "nombre": articulo["Nombre"],
            "tema": articulo["Contenido_Articulo"][0][0].split(":")[0].strip(),
            "contenido": articulo["Contenido_Articulo"], 
            "fecha": articulo["Fecha_Articulo"]
        } 

        for articulo in coleccion_articulo.find({}).sort("_id", -1)
    ]

    # Obtener los datos de usuario
    datos_usuarios = [dato["Nombre"] for dato in coleccion_usuario.find({})]

    # Rutas de la pagina

    @app.route("/")
    def index():
        return render_template("index.html", articulos = articulos, 
            enumerate = enumerate, nombre = session.get("Usuario", ""))

    @app.route("/Crear_Articulo", methods = ["GET", "POST"])
    def crear_articulo():

        if request.method == "POST":

            contenido = [request.form.get("contenido")]
            contenido_dividido = [oracion.split("\r\n") for oracion in contenido]
            fecha = datetime.now().strftime("%d/%m/%Y")

            print(contenido_dividido[0][0].split(":")[0].strip())

            # Subir los datos a la bbdd
            coleccion_articulo.insert_one({"Nombre": contenido_dividido[0][0].split(":")[0].strip(), 
                "Contenido_Articulo": contenido_dividido, "Fecha_Articulo": fecha})
            print("Se enviaron los datos! \U0001F642")

        return render_template("Crear_Articulo.html", nombre = session.get("Usuario", ""))

    @app.route("/Mis_Articulos")
    def mis_articulos():
        return render_template("Mis_Articulos.html", articulos = articulos, 
            nombre = session.get("Usuario", ""))

    @app.route("/borrar_articulo/<titulo_articulo>", methods = ["POST"])
    def borrar_articulo(titulo_articulo):
        
        # Eliminar el artículo de la colección basado en su tema
        resultado = coleccion_articulo.delete_one({"Nombre": titulo_articulo})
        
        if resultado.deleted_count < 0:
            return f"Artículo '{titulo_articulo}' no encontrado \U0001F612", 404

        print(f"Artículo '{titulo_articulo}' eliminado \U0001F642")
        return redirect(url_for("mis_articulos"))

    @app.route("/<titulo_articulo>")
    def pagina_articulo(titulo_articulo):
        articulo_encontrado = next((articulo for articulo in articulos if articulo["tema"] == titulo_articulo), None)
        
        if articulo_encontrado:

            # Dividir los subtitulos y los contenidos
            contenido = articulo_encontrado["contenido"][0]

            subtitulos_articulo = [linea for linea in contenido if len(linea) < 80 and len(linea) != 0]
            contenido_articulo = [linea for linea in contenido if len(linea) > 70]

            # Crear estructura para guardarlos
            articulos_procesados = [
                {"subtitulo": subtitulo, "contenido": contenido}
                for subtitulo, contenido in zip(subtitulos_articulo, contenido_articulo)
            ]

            # Obtener los comentarios relacionados con el tema del artículo
            coleccion_comentarios = app.db["Comentarios"]
            comentarios = list(coleccion_comentarios.find({"Tema": titulo_articulo}))

            return render_template("Plantilla_Articulos.html", temas = titulo_articulo, 
                articulos_procesados = articulos_procesados, comentarios = comentarios, 
                nombre = session.get("Usuario", ""))
        else:
            abort(404)

    # Seccion de comentarios

    @app.route("/Agregar_Comentario", methods = ["POST"])
    def agregar_comentario():
        comentario = request.form.get("comentario")
        tema = request.form.get("tema")
        
        if comentario and tema:
            coleccion_comentarios = app.db["Comentarios"]
            coleccion_comentarios.insert_one({"Tema": tema, "Comentario": comentario, 
                "Fecha": datetime.now()})
        
        return redirect(url_for("pagina_articulo", titulo_articulo = tema))

    @app.route("/Seccion_Chatbots")
    def seccion_chatbots():
        return render_template("Seccion_Chatbots.html", nombre = session.get("Usuario", ""))

    @app.route("/Sobre_Nosotros")
    def sobre_nosotros():
        return render_template("Sobre_Nosotros.html", nombre = session.get("Usuario", ""))

    @app.route("/Login", methods = ["GET", "POST"])
    def login():

        if request.method == "POST":

            nombre = request.form.get("nombre-usuario")
            email = request.form.get("correo")
            contraseña = request.form.get("clave")

            # Verificar si el usuario ya existe
            usuario_existente = coleccion_usuario.find_one({"Email": email})

            if usuario_existente:
                # Comparar la contraseña o mostrar un mensaje de error
                if usuario_existente["Contraseña"] == contraseña:
                    session["Usuario"] = usuario_existente["Nombre"]
                else:
                    print("Contraseña incorrecta")
                    # Redirigir a la página de inicio de sesión con un mensaje de error
                    return redirect(url_for("login"))
            else:
                # Guardar el usuario en la base de datos
                coleccion_usuario.insert_one({"Nombre": nombre, "Email": email, 
                    "Contraseña": contraseña})
                
                session["Usuario"] = nombre
                print("Se enviaron los datos! \U0001F642")
            
            return redirect(url_for("index"))
        return render_template("Inicio_Sesion.html", nombre = session.get("Usuario", ""))

    @app.errorhandler(404)
    def error_404(e):
        return render_template("404.html"), 404

    return app

if __name__ == "__main__":
    app = informatikspace()
    app.run()