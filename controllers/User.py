import hashlib

from models.UserModel import UserModel
from libraries.Geo import Geo

class User:

	def createUser(self,nombres,apellidos,direccion,ciudad):
		if len(nombres) < 1 :
			json = {
				'error': 'error',
				'reason': 'Nombres son requeridos'
			}

			return json

		if len(apellidos) < 1 :
			json = {
				'error': 'error',
				'reason': 'Apellidos son requeridos'
			}

			return json

		if len(direccion) < 1 :
			json = {
				'error': 'error',
				'reason': 'Dirección es requerida'
			}

			return json

		if len(ciudad) < 1 :
			json = {
				'error': 'error',
				'reason': 'ciudad es requerida'
			}

			return json

		id = str(nombres+'-'+apellidos)
		id = hashlib.md5(id.encode('utf-8')).hexdigest()

		obj = {
			'_id'           : id,
			'nombres' : nombres,
			'apellidos' : apellidos,
			'direccion' : direccion,
			'ciudad' : ciudad,
			'estadogeo':None
		}

		u = UserModel()

		data = u.createUser(obj)

		try:
			ok = data['ok']
			return data
		except:
			return data

	def getUserById(self,id):
		u = UserModel()

		data = u.getUserById(id)

		if data['bookmark'] == 'nil':
			json = {
				'error':'error',
				'reason':'Id de usuario Incorrecta'
			}

			return json

		return data

	def deleteUser(self,id):
		u = UserModel()

		data = u.getUserById(id)

		obj = {
			'_id'     : id,
			'_rev'    : data['docs'][0]['_rev']
		}

		data = u.deleteUser(obj)
		return data

	def getAllUsers(self):
		u = UserModel()

		data = u.getAllUsers()
		return data


	def codificarBase(self):
		u = UserModel()

		data = u.getAllUsers()

		q_rows = str(data['total_rows'])
		q_rows = int(q_rows)
		rows = data['rows']
		for i in range(q_rows):
			if rows[i]['doc']['estadogeo'] == None:
				coords = self.addBase(rows[i])
				if coords:
					rows[i]['doc']['estadogeo'] = True
					rows[i]['doc']['latitud'] = coords['results'][0]['geometry']['location']['lat']
					rows[i]['doc']['longitud'] = coords['results'][0]['geometry']['location']['lng']
					return self.updateCoords(rows[i]['doc'])
			else:
				pass

		json = {
			'loading':True,
			'reason':'Cargando Coordenadas'
		}

		return json

	def addBase(self,user):
		self.db = Geo()

		obj = {
			'direccion': user['doc']['direccion'],
			'ciudad': user['doc']['ciudad']
		}

		data = self.db.getCoords(obj)

		if data["status"] == "ZERO_RESULTS":
			return None

		return data

	def updateCoords(self,user):
		u = UserModel();
		data = u.createUser(user)

		try:
			ok = data['ok']
			return data
		except:
			return data


		return user
