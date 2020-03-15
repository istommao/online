"""app urls."""
from django.urls import path

from app import views

app_name = 'app'


urlpatterns = [
    path('idcard/', views.IDCardView.as_view(), name='idcard_view'),
]
