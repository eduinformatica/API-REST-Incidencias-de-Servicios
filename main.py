'''
	Este archivo principal es el que estara encargado de
	arrancar nuestra aplicacion
'''
# Importamos los recursos a ulitilizar
from flask import Flask, jsonify, request
from incidencias import incidencias

# Intanciamos el objeto Flask
app = Flask(__name__)

@app.route("/incidencias")
def getIncidencias():
	return jsonify({"Incidencias": incidencias})

@app.route("/incidencias", methods=["POST"])
def addIncidencia():
	new_incidencia = {
		"fecha": request.json["fecha"],
		"titulo": request.json["titulo"],
		"descripcion": request.json["descripcion"],
		"agente": request.json["agente"]
	}
	incidencias.append(new_incidencia)
	return jsonify({"mensaje": "nueva incidencia agregada", "Incidencias": incidencias})

if __name__ == "__main__":
	app.run(port=5000, debug=True)