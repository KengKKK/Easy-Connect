from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader

from connect import ShowLog

from .form import CallScript,ConnectSwitch

# Create your views here.


def my_view(request):
    return render(request, 'pages/connect.html')

def show(request):
    return render(request, 'pages/show.html')

def func(request):
       return render(request, 'pages/function.html')

def callScript(request):
        if request.method == 'POST':
         form = CallScript(request.POST)
        if form.is_valid():
            ShowLog()
            return HttpResponseRedirect('show')

def connectSwitch(request):
        if request.method == 'POST':
         form = ConnectSwitch(request.POST)
        if form.is_valid():
            ShowLog()
            return HttpResponseRedirect('show')




