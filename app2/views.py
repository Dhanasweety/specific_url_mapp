from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def first(request):
    return HttpResponse('<marquee><h1>Bangaru read well ma...</h1></marquee>')

def second(request):
    return HttpResponse('<h1>chandani is a allari pilla</h1>')