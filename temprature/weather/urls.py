from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^cityname/(?P<city_name>\w+)$', views.get_weather_city, name='get_weather_city'),
	url(r'^cityzip/(?P<city_zipcode>\d+)$', views.get_weather_cityzip, name='get_weather_cityzip'),
]