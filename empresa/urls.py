from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views




urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
    path('sobre-nosotros/', views.sobrenosotros, name="sobre-nosotros"),
	path('servicios/', views.servicios, name="servicios"),
	path('serviciospagina2/', views.serviciospagina2, name="serviciospagina2"),
	path('contacto/', views.contacto, name="contacto"),
	path('contactopass/', views.contactopass, name="contactopass"),
	path('servicios/', views.servicios, name="servicios"),
	path('politicas/', views.politicas, name="politicas"),
	path('politica-cookies/', views.politicacookies, name="politica-cookies"),

]