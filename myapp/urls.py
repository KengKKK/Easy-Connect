from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('connect', views.connect),
    path('', views.login),
]