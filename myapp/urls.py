from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.function),
    path('connect', views.connect),
    path('', views.login),
]