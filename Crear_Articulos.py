
import json
from llamaapi import LlamaAPI
from flask import Flask, render_template

# Instancia de Flask
app = Flask(__name__)

# Inicializar la biblioteca de IA
llama = LlamaAPI("LL-0BmJ3NWVQbnUWUFiMDlUhyyJTeFpYV4qPM6yOTjIBGigjdd3QVGJJKlMR7JdE6Gz")

# Contextos de los modelos
contenido = open("ContextoModelo/Contexto_Contenido.txt", "r").read()
navegacion = open("ContextoModelo/Contexto_Navegacion.txt", "r").read() 

def estructura_modelo(contexto, prompt):
	consulta = {
		"model": "llama-70b-chat",
		    "messages": [
		      {"role": "user", "content": prompt},
		      {"role": "function", "name": "function_description", "content": contexto}
		    ],

		"max_tokens": 1500,   
	    "temperature": 0.7,   
	    "top_p": 0.9,    
	    "stream": False 
	}

	# Ejecutar la consulta
	respuesta = llama.run(consulta)
	print(json.dumps(respuesta.json()["choices"][0]["message"]["content"]))

def generar_contenido():
	return estructura_modelo(contenido, "Quiero que mi blog sea sobre BTS, quienes son, su evolucion, carrera, fandom")

def generar_navegacion():
	return estructura_modelo(navegacion + "Quiero que mi blog sea sobre BTS, quienes son, su evolucion, carrera, fandom", contenido)

# generar_contenido()
# generar_navegacion()




# if __name__ == "__main__":
# 	app.run()