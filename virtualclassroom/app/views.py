from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")

def login(request):
    return render(request, 'app/login.html')

def dashboard(request):
    return render(request, 'app/dashboard.html')

def lecture(request):
    return render(request, 'app/lecture.html')
