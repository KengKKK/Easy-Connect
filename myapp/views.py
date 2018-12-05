from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from connect import ShowLog,Shell

from .form import CallScript, ConnectSwitch

# Create your views here.


def home(request):
    return render(request, 'home.html')


def show(request):
    return render(request, 'pages/show.html')


def func(request):
    return render(request, 'pages/function.html' ,data)



# function
def callScript(request):
    if request.method == 'POST':
        inventory = request.POST.get('inventory')
        inv = inventory
        Version = request.POST.get('Version')
        ver = Version
        Environment = request.POST.get('Environment')
        env = Environment
        CPU = request.POST.get('CPU')
        cpu = CPU
        Memory = request.POST.get('Memory')
        mem = Memory
        Clock = request.POST.get('Clock')
        clk = Clock
        System = request.POST.get('System')
        sys = System
        Neighbors = request.POST.get('Neighbors')
        neb = Neighbors
        Vlan = request.POST.get('Vlan')
        vlan = Vlan
        Interface = request.POST.get('Interface')
        inf = Interface

    if inv == 'on':
        print(inv)
        f = open("config/Inventory.txt", "w")
        f.writelines([inv])
        f.close()

    if ver == 'on':
        print(ver)
        f = open("config/Version.txt", "w")
        f.writelines([ver])
        f.close()
    if env == 'on':
        print(env)
        f = open("config/Environment.txt", "w")
        f.writelines([env])
        f.close()
    if cpu == 'on':
        print(cpu)
        f = open("config/CPU.txt", "w")
        f.writelines([cpu])
        f.close()
    if mem == 'on':
        print(mem)
        f = open("config/Memory.txt", "w")
        f.writelines([mem])
        f.close()
    if clk == 'on':
        print(clk)
        f = open("config/Clock.txt", "w")
        f.writelines([clk])
        f.close()
    if sys == 'on':
        print(sys)
        f = open("config/System.txt", "w")
        f.writelines([sys])
        f.close()
    if neb == 'on':
        print(neb)
        f = open("config/Neighbors.txt", "w")
        f.writelines([neb])
        f.close()
    if vlan == 'on':
        print(vlan)
        f = open("config/Vlan.txt", "w")
        f.writelines([vlan])
        f.close()
    if inf == 'on':
        print(inf)
        f = open("config/Interface.txt", "w")
        f.writelines([inf])
        f.close()

        # print(inventory,Version,Environment,CPU,Memory,Clock,System,Neighbors,Vlan,Interface)
    return render(request, 'pages/show.html')


# connect
def connectSwitch(request):
    if request.method == 'POST':
        Shell()
        Ip = request.POST.get('Ip')
        f = open("config/IpPort.txt", "w")
        f.writelines(['telnet ', Ip])
        f.close()
        global data 
        data = {
            'ip': Ip,
        }
    return render(request, 'pages/show.html' ,data)
