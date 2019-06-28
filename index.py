#importamos la liberia de Flask
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Damos rutas (url´s) al sio web
#Le decimos que la ruta princiapl es el index con ('/')
@app.route('/')
def home(): #funcion que maneja la ruta
	#return 'Home page' #retorna algo
	return render_template('home.html')

#Mas rutas del sitio
@app.route('/about')
def about():
	#return 'About page'
	return render_template('about.html')


#Siempre atento a peticiones del sevidor
if __name__ == '__main__':
	app.run(debug=False)