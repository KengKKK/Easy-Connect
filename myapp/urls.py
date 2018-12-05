from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('admin/', admin.site.urls),
    path('account/',include('django.contrib.auth.urls')), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('connect', login_required(TemplateView.as_view(template_name='pages/connect.html'))),
    
    path('func', login_required(views.func)),
    path('show', login_required(views.show)),  

    # function
    path('callScript', login_required(views.callScript)), 
    # connect
    path('connectSwitch', login_required(views.connectSwitch)), 
]