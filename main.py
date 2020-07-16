'''
	Este archivo principal es el que estara encargado de
	arrancar nuestra aplicacion
'''
# Importamos los recursos a ulitilizar
from flask import Flask, jsonify, request
from incidents import incidents

# Intanciamos el objeto Flask
app = Flask(__name__)

@app.route('/incidents')
def getIndex():
	return jsonify({'Incidencias': incidents})
	# return "";

@app.route('/incidents', methods=['POST'])
def addIncidents():
	new_incidents = {
		"fecha": request.json['fecha'],
		"titulo": request.json['titulo'],
		"descripcion": request.json['descripcion'],
		"agente": request.json['agente']
	}
	incidents.append(new_incidents)
	
	return jsonify({'message': 'add new incidents', 'Incidencias': incidents})
	

if __name__ == '__main__':
	app.run(port=5000, debug=True)