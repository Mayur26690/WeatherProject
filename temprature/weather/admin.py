# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models


class CityAdmin(admin.ModelAdmin):
	list_display = ('city_name', 'city_zipcode')


class WeatherAdmin(admin.ModelAdmin):
	list_display = ('city', 'temp', 'cloudy')




# Register your models here.
admin.site.register(models.Weather, WeatherAdmin)
admin.site.register(models.City, CityAdmin)

