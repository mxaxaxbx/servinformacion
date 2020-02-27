from flask import session

from libraries.couchdb import Couchdb

import json

class UserModel(object):
	
	def __init__(self):
		super(UserModel, self).__init__()
		self.db = Couchdb('servinformacion')

	def getUser(self,email,password):
		self.db.name = 'users'

		array = {
			'selector': {
				'$and': [
      				{ 'email': email },
      				{ 'password': password }
    			]
			},
			'fields': ['_id', '_rev','name','email','profilePhoto']
		}

		data = self.db.find(array)

		return data

	def getCurrentUser(self):
		array = {
			'selector': {
				'_id': session['_id']
			},
			'fields': ['_id','_rev','cellphone','email','last_name','name']
		}

		data = self.db.find(array)

		return data

	def getAllUsers(self):
		data = self.db.getAll()

		return data

	def updateData(self,obj):
		data = self.db.create(obj)

		return data

	def getUserById(self,id):
		array = {
			'selector': {
				'_id': id
			},
		}

		data = self.db.find(array)

		return data

	def deleteUser(self,obj):
		data = self.db.delete(obj)
		return data

	def createUser(self,obj):
		data = self.db.create(obj)

		return data