from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required

urlpatterns = [

   path('admin/', admin.site.urls),
   path('account/',include('django.contrib.auth.urls')),
   path('', TemplateView.as_view(template_name='registration/login.html')),    


    path('test', login_required(views.my_view)), 
]