import requests
import json
import urllib.parse

class Geo(object):

	name = ''
	url = ''
	
	def __init__(self):
		super(Geo, self).__init__()

	def getCoords(self,obj):
		obj['direccion'] = urllib.parse.quote(obj['direccion'])
		obj['ciudad'] = urllib.parse.quote(obj['ciudad'])
		data = self.curl(obj)
		return data

	
	def curl(self,obj):
		
		payload = json.dumps(obj)

		headers = {
			'Content-Type': 'application/json',
			'Accept-Charset': 'utf8'
		}
		url = 'https://maps.googleapis.com/maps/api/geocode/json?'+'address='+obj['direccion']+' '+obj['ciudad']+'&'+'key=AIzaSyB0PLLiELJiVb1INOoJI3ye0ZAtLzbRGCs'
		
		response = requests.get(url)

		return response.json()