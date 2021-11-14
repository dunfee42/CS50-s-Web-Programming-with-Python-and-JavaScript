from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brain(request):
    return HttpResponse("Hello, Brian")

#this medthod allows the rendering of a whole HTML template which can have styling and much more..
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")