import requests
import json

class Couchdb(object):

	name = ''
	url = ''
	
	def __init__(self,name):
		super(Couchdb, self).__init__()
		self.name = name
		self.url = 'http://127.0.0.1:5984/'+name+'/'

	def find(self,array):
		method = 'POST'
		data = self.curl(array,method)
		return data

	def create(self,array):
		method = 'PUT'
		data = self.curl(array,method)
		return data;

	def delete(self,obj):
		method = 'DELETE'
		data = self.curl(obj,method)
		return data

	def getAll(self):
		method = 'GET'
		obj = {}
		data = self.curl(obj,method)
		return data
		
	def curl(self,array,method):
		
		payload = json.dumps(array)

		headers = {
			'Content-Type': 'application/json',
			'Accept-Charset': 'utf8'
		}
		if method == 'POST':
			response = requests.post(self.url+'_find',headers=headers,data=payload)
		elif method == 'PUT':
			response = requests.put(self.url+'/'+array['_id'],headers=headers,data=payload)
		elif method == 'DELETE':
			response = requests.delete(self.url+'/'+array['_id']+'/?rev='+array['_rev'],headers=headers,data=payload)
		elif method == 'GET':
			response = requests.get(self.url+'/_all_docs?include_docs=true',headers=headers,data=payload)

		return response.json()