# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
	city_name = models.CharField(max_length=45)
	city_zipcode = models.PositiveIntegerField()

	def __str__(self):
		return self.city_name


# Create your models here.
class Weather(models.Model):
	city = models.OneToOneField(City)
	temp = models.IntegerField()
	cloudy = models.CharField(max_length=20)

	def __str__(self):
		return str(self.temp)