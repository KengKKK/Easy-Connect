from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
 return render(request, 'index.html')

def function(request):
    template = loader.get_template("function.html")
    return HttpResponse(template.render())

# def login(request):
#     data = {
#         'user':"eiei",
#         'password':"kk",
#     }
#     return render(request, 'login.html',data)

def connect(request):
    template = loader.get_template("connect.html")

    return HttpResponse(template.render())
