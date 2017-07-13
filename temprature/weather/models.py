# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	city_name = models.CharField(max_length=45)
	city_zipcode = models.PositiveIntegerField()

	def __str__(self):
		return self.city_name
	# weather_temp = models.ForeignKey('Weather', on_delete=models.CASCADE)
	# weather_

# Create your models here.
class Weather(models.Model):
	city = models.OneToOneField(City)
	temp = models.IntegerField()
	cloudy = models.CharField(max_length=20)

	def __str__(self):
		return self.temp, self.cloudy