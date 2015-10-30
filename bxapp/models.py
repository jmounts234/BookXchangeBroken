from django.db import models

class User(models.Model):
	email = models.CharField(max_length = 1234)
	password = models.CharField(max_length=120)

class Sale(models.Model):
	isbn = models.CharField(max_length=13)
	seller = models.EmailField()

class Book(models.Model):
	isbn = models.CharField(max_length=13)
	rawjson = models.CharField(max_length=500)

	def __unicode__(self):
		return self.isbn

	def get_isbn(self):
		return self.isbn

	def get_json(self):
		import json
		return json.loads(self.rawjson)

	def title(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['title']
		except:
			return "no title"

	def description(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['description']
		except:
			return "no description"

	def year(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['publishedDate']
		except:
			return "no year"

	def subtitle(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['subtitle']
		except:
			return "no subtitle"

	def authors(self):
		try:
			data = self.get_json()
			return ", ".join(data['items'][1]['volumeInfo']['authors'])
		except:
			return "no authors"

	def cover(self):
		try:
			data = self.get_json()
			return data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
		except:
			return "no cover"