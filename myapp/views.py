from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def index(request):
#  return render(request, 'index.html')
def index(request):
    data = {
        'user':"Enter User",
        'password':"Enter Password",
    }
    return render(request, 'index.html',data)

def function(request):
    return render(request, 'function.html')

def connect(request):
    return render(request, 'connect.html')



