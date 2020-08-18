from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>welcome!</h1>")


def aboutus(request):
    return HttpResponse("name :uthej <hr> roll:1602-18-737-56")


def myhobbies(request):
    return HttpResponse("hobbies:playing cricket,watching series")


def index(request):
    return HttpResponse("<h1>hello</h1>")
