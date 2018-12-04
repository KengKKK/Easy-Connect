from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from connect import ShowLog

# Create your views here.


def my_view(request):

    return render(request, 'test.html')


def func(request):
        template = loader.get_template("pages/function.html")
        ShowLog()
        return HttpResponse(template.render(ShowLog(),request))



