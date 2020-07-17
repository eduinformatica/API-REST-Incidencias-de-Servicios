# API-REST-Incidencias-de-Servicios.

API REST que expone a traves de HTTP utlilizando JSON para el <br />
traspaso de mensajes.


## Requisitos.

En este apartado se especificara todo lo necesario para ejecutar de forma
local esta aplicacion.

1. Lenguaje [Python](https://www.python.org/downloads/)
2. Framework [Flask](https://flask.palletsprojects.com/en/master/installation)
3. Editor de Codigo, el que me le acomode a usted
	* [Sublime Text 3](https://www.sublimetext.com)
	* [Visual Studio Code](https://code.visualstudio.com)
	* [Brackets](https://brackets.io/)
	* [Atom](https://atom.io)
	* [Notepad++ v7.8.8](https://notepad-plus-plus.org/downloads/v7.8.8/)

### Instalacion de Flask en Windows
```batch
	> pip install Flask
```

### Instalacion de Flask en GNU/Linux
```bash
	$ pip install Flask
```
> **Nota:** Ingresar como root para instalar el framework


## Instrucciones para su ejecucion en un entorno local

1. Creamos un directorio en el escritorio con el nombre "API-REST-Incidencias-de-Servicios".
2. Dentro del direcctorio ejcutamos el archivo principal main.py en la que se encarga de iniciar <br /> 
nuestra aplicacion en el puerto 5000.
3. Al arrancar la aplicacion escribimos el siguiente link: http://localhost:5000/incidencias.
4. Como paso final podemos testear agregando una nueva incidencia en formato JSON (JavaScript Object Notation).

## Postman

[Documentacion de Postman](https://info-developer.postman.co/collections/12074220-0cd59dd3-490d-4ae0-9c86-5d08a03d1d5e?version=latest&workspace=574f1914-d365-49d7-8493-ffa8ac41171c)