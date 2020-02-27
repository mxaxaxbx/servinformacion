# -*- coding: utf-8 -*-
from controllers.User import User

from flask import Flask,request,session,request,redirect,url_for,flash

import hashlib

app = Flask(__name__)
app.secret_key = 'random'

class App:
	
	@app.route('/crear',methods=['POST'])
	def crear():
		if request.method == 'POST':
			nombres = request.form['nombres']
			apellidos = request.form['apellidos']
			direccion = request.form['direccion']
			ciudad = request.form['ciudad']

			u = User()
			return u.createUser(nombres,apellidos,direccion,ciudad)
		else:
			json = {
				'error': 'error',
				'reason': 'Method Not Allowed'
			}
			return json
	
	@app.route('/lista',methods=['GET'])
	def lista():
		u = User()
		return u.getAllUsers()

	@app.route('/usuario/<id>',methods=['GET'])
	def usuario(id):
		u = User()
		return u.getUserById(id)

	@app.route('/eliminar/<id>',methods=['GET','DELETE'])
	def eliminar(id):
		if request.method == 'DELETE':
			u = User()
			return u.deleteUser(id)
		else:
			json = {
				'error': 'error',
				'reason': 'Method Not Allowed'
			}
			return json

	@app.route('/geocodificar_base',methods=['GET'])
	def codificarBase():
		u = User()
		return u.codificarBase()



if __name__ == '__main__':
	app.run(debug=True)