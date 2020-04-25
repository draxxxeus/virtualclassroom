from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello potters!!</h1>")

def login(request):
    return render(request, 'app/login.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

def lecture(request):
    return render(request, 'app/lecture.html')
