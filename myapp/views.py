from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def function(request):
    template = loader.get_template("function.html")

    return HttpResponse(template.render())

def login(request):
    template = loader.get_template("login.html")
    data = {
        'user':"tets",
        'password':"test",
    }
    return HttpResponse(template.render(data,request))

def connect(request):
    template = loader.get_template("connect.html")

    return HttpResponse(template.render())
