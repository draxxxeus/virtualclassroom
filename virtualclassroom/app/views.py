from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello potters!!</h1>")

def list_all_lectures(request):
    pass
# Create your views here.
