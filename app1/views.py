from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style = 'color:blue'> Hello, World! This is my first Django app.</h1>")
