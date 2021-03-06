class createbook:
	def __init__(self, isbn):
		self.isbn = isbn

	def validate_isbn(self):
		# if len(self.isbn) != 13:
		# 	if len(self.isbn) != 10:
		# 		return False 
		# for n in self.isbn:
		# 	if n not in "1234567890": return False
		return True

	def make(self):
		if not self.validate_isbn(): return False
		from .models import Book
		book = Book(isbn=self.isbn, rawjson=self.get_rawjson())
		return book

	def get_rawjson(self):
		import urllib
		return urllib.urlopen(self.gen_url()).read()

	def gen_url(self):
		return "https://www.googleapis.com/books/v1/volumes?q=isbn:" + "9780671707743"

class createuser:
	def __init__(self, email, password):
		self.email = email
		self.password = password

	def signUp(self):
		from .models import User
		user = User(email = self.email, password = self.password)
		return user