from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template("index.html")

    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    data = {
        'user':"admin",
        'password':"admin",
    }
    return HttpResponse(template.render(data,request))

def connect(request):
    template = loader.get_template("connect.html")

    return HttpResponse(template.render())
