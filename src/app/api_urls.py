"""app urls."""
from django.urls import path

from app import apis

app_name = 'app'


urlpatterns = [
    path('car/', apis.CarSearchAPI.as_view(), name='car_search'),
    path('httpcode/', apis.HttpCodeSearchAPI.as_view(), name='httpcode_search'),
    path('short_url/', apis.ShortUrlCodeAPI.as_view(), name='short_url')
]
