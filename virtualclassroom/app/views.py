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
    if request.method == 'GET':
        if request.session.get('user_id', False) and request.session.get('role') != 'student':
            courses = Course.get_courses(request.session.get('user_id'))
            context = {'courses': courses}
            return render(request, 'upload.html', context)
        else:
            return HttpResponseRedirect(reverse('login'))
    elif request.method == 'POST':
        if request.session.get('user_id', False) and request.session.get('role') != 'student':
            lecture_form = UploadLectureForm(request.POST)
            recording = request.FILES.getlist('recording')[0]
            notes = request.FILES.getlist('notes')

            if lecture_form.is_valid():
                lecture = lecture_form.save(commit=False)
                lecture.index = Lecture.objects.filter(course=lecture.course).order_by('-index')[:1][0].index + 1
                lecture.teacher = request.user
                lecture.save()

                resource_recording = Resource(
                        media=recording,
                        type='R',
                        lecture=lecture,
                        publish_on=lecture.publish_on,
                        complete_by=lecture.complete_by
                        )
                resource_recording.save()

                for note in notes:
                    resource_notes = Resource(
                            media=note,
                            type='A',
                            lecture=lecture,
                            publish_on=lecture.publish_on,
                            complete_by=lecture.complete_by
                            )
                    resource_notes.save()
            else:
                print("invalid form")


            return HttpResponseRedirect(reverse('lecture'))
        else:
            return HttpResponseRedirect(reverse('login'))
