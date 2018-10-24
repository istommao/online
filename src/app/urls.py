"""app urls."""
from django.urls import path

from app import apis

app_name = 'app'


urlpatterns = [
    path('car/', apis.CarSearchAPI.as_view(), name='car_search'),
]
