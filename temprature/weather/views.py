# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def get_weather_city(request, city_name):
	city = models.City.objects.get(city_name=city_name)
	weather = models.Weather.objects.get(city=city)
	return render(request, 'weather/temp.html', {"city": city, "weather":weather})


def get_weather_cityzip(request, city_zipcode):
	city = models.City.objects.get(city_zipcode=city_zipcode)
	weather = models.Weather.objects.get(city=city)
	return render(request, 'weather/temp.html', {"city": city, "weather": weather})