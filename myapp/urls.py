from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('function/', views.function),
    path('connect', views.connect),
    path('login', views.login),
    
]