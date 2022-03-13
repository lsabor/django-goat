from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
# takes request -> returns response
# it's a request handler
# some frameworks it's called 'action', weird nomenclature


def say_hello(request):
    # we really can do anything here:
    # Pull data from db
    # Transform
    # Send email
    return render(request,'hello.html',{'name': 'babadook'})


def say_goodbye(request):
    f = 'fartbag'
    g = [1,2,3]
    return HttpResponse(f'{f = }, the code is: {g}')

def hi(request):
    x = calculate()
    return HttpResponse(f'{x = }, the code is: {x+1}')

def calculate():
    x = 1
    y = 2
    return x+y