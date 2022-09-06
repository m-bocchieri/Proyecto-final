from typing import Dict

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio (request):

    return render (request , "App/inicio.html")

def modelo1 (request):

    return render (request, "App/modelo1.html")

def modelo2 (request):
    
    return render (request, "App/modelo2.html")

def modelo3 (request):

    return render (request, "App/modelo2.html")