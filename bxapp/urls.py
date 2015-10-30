from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='overview'),
  url(r'^overview/$', views.overview, name='overview'),
  url(r'^signin/$', views.signUp, name='signUp'),
  url(r'^signUp/$', views.signin, name='signin'),
  url(r'^purchase/$', views.overview, name='purchase'),
  url(r'^addBook/$', views.addBook, name='addBook'),
  url(r'^bookAdded/$', views.addBook, name='bookAdded')

]