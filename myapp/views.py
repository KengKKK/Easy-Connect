from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from talk import Switch
from .form import  ConnectSwitch

# Create your views here.
global data 

def home(request):
    return render(request, 'home.html')


def show(request):
    return render(request, 'pages/show.html')


# connect
def connectSwitch(request):
    if request.method == 'POST':        
        Ip = request.POST.get('Ip')
        user = request.POST.get('user')
        passw = request.POST.get('passw')
        # Switch(Ip,user,passw)

        f = open("Output.txt","r")
        output = f.read()
        f.close()

        data = {
            'output' : output,
        }
     
    return render(request, 'pages/show.html' ,data)
