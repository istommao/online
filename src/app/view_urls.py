"""app urls."""
from django.urls import path

from app import views

app_name = 'app'


urlpatterns = [
    path('idcard/', views.IDCardView.as_view(), name='idcard_view'),
    path('catblog/', views.CatBlogDemoView.as_view(), name='catblog_demo_view'),
]
