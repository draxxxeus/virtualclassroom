from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def lecture(request):
    return render(request, 'lecture.html')

def pricing(request):
    return render(request, 'pricing.html')
