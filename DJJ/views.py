from django.shortcuts import render
from . import corona

def index(request):
    x,state,Total = corona.coro()
    l = {'a' : x  , 'b' : Total , 'c': state}
    return render(request,'corona.html', l)
