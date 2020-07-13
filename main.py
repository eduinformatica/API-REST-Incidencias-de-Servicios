'''
	Este archivo principal es el que estara encargado de
	arrancar nuestra aplicacion
'''
# Importamos los recursos a ulitilizar
from flask import Flask, jsonify

# Intanciamos el objeto Flask
app = Flask(__name__)

# Pantalla principal al iniciar nuestra aplicacion
@app.route("/")
def Index():

	return ""


if __name__ == "__main__":
	app.run(port=5000, debug=True)