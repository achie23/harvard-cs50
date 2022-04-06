from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello Django World!")

def second(request):
    return HttpResponse("Second Page")

def third(request):
    return HttpResponse("Third Page")