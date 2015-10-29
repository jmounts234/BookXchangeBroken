from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from .models import *
from .helpers import *

def index(request):
	return overview(request)

def overview(request):
	try:
		mail = request.COOKIES['mail']
	except:
		mail = None

	try:
		books = Book.objects.all()
		template = loader.get_template('overview.html')
		context = RequestContext(request, { 'books' : books, 'name' : mail }) 
		return HttpResponse(template.render(context))
	except:
		return HttpResponse("The page you've selected does not exist.")

def signUp(request):
	if(request.GET.get('signUp')):
		email = request.GET.get('email')
		password = request.GET.get('password')	
		try:
			createuser(email, password).signUp()
		except:
			return HttpResponse("User name is already in use.")
		template = loader.get_template('overview.html')
	else:
		template = loader.get_template('signup.html')

	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


def signin(request):
	context = RequestContext(request, {})

	if(request.GET.get('signin')):
		email = request.GET.get('email')
		password = request.GET.get('password')	

		template = loader.get_template('overview.html')
		response = HttpResponse(template.render(context))
		response.set_cookie('mail', email, max_age = 100)
	else:
		template = loader.get_template('signin.html')
		return HttpResponse(template.render(context))

	return response


def purchase(request):
	template = loader.get_template('purchase.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def addBook(request):
	if(request.GET.get('addBook')):
		isbn = request.GET.get('isbn')
		createbook(isbn).make()
		template = loader.get_template('overview.html')
	else:
		template = loader.get_template('addBook.html')

	context = RequestContext(request, {})
	return HttpResponse(template.render(context))



