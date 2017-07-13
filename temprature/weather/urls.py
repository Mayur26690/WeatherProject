from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
	
	url(r'^losangeles/$',views.getWeatherLA),
	url(r'^sanfransisco/$',views.getWeatherSF),
	url(r'^chicago/$',views.getWeatherChicago),
	url(r'^90029/$',views.getWeatherLA),
	url(r'^90028/$',views.getWeatherSF),
	url(r'^90027/$',views.getWeatherChicago),
]