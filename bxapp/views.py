from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from .models import *
from .helpers import *

def index(request):
	return overview(request)

def overview(request):
	# from .helpers import createbook
	# createbook('9780553293357').make()
	# createbook('9780131103627').make()
	
	try:
		books = Book.objects.all()
		template = loader.get_template('overview.html')
		context = RequestContext(request, { 'books' : books })
		return HttpResponse(template.render(context))
	except:
		return HttpResponse("The book you've selected does not exist.")

def signUp(request):
	context = RequestContext(request, {})
	if(request.GET.get('signUp')):
		email = request.GET.get('email')
		password = request.GET.get('password')
		#try:
		createuser(email, password).signUp()
		#except:
		#	return HttpResponse("User name is already in use.")
		template = loader.get_template('thankyou.html')
		return HttpResponse(template.render(context))
	else:
		template = loader.get_template('signup.html')

	return HttpResponse(template.render(context))

def purchase(request):
	template = loader.get_template('purchase.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def addBook(request):
	context = RequestContext(request, {})

	if(request.GET.get('addBook')):
		isbn = request.GET.get('isbn')
		createbook(isbn).make()
		#if(createbook(isbn).make()):
		#	template = loader.get_template('bookAdded.html')
		#	return HttpResponse(template.render(context))
		#else:
		#	return HttpResponse("Invalid ISBN")
	else:
		template = loader.get_template('addBook.html')

	return HttpResponse(template.render(context))



