from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>hii mom how ruu....</h1>')

def second(request):
    return HttpResponse('<h1>Hiii chandani,shahanaj today im full happy im gng to home</h1>')