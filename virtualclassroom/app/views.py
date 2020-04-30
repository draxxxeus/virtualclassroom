from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    return render(request, "index.html")

def login(request):
    if request.session.get('user_id', False):
        return render(request, 'dashboard.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                request.session['user_id'] = str(user.id)
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'login.html')

def dashboard(request):
    if request.session.get('user_id', False):
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def lecture(request):
    if request.session.get('user_id', False):
        return render(request, 'lecture.html')
    else:
        return HttpResponseRedirect(reverse('login'))

def pricing(request):
    return render(request, 'pricing.html')

def logout(request):
	try:
		del request.session['user_id']
	except KeyError:
		pass

	return HttpResponseRedirect(reverse('login'))

def upload(request):
    if request.session.get('user_id', False) and request.session.get('role') != 'student':
        return render(request, 'upload.html')
    else
        return HttpResponseRedirect(reverse('login'))
