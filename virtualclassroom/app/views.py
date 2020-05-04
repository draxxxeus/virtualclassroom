from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Course, Discussion, Lecture, Notifications, Resource
from .forms import UploadLectureForm


def index(request):
    return render(request, "index.html")


def login_user(request):
    if request.method == 'GET':
        if request.session.get('user_id', False):
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = str(user.id)
                request.session['role'] = user.role
                return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid email or password.')
            return HttpResponseRedirect(reverse('login'))


@login_required
def dashboard(request):
    context = Lecture.get_lectures_for_user(user=request.user)
    return render(request, 'dashboard.html', context)


@login_required
def lecture(request):
    lecture_id = request.GET.get('id', False)

    context = Lecture.get_lecture(lecture_id=lecture_id, user=request.user)
    if context:
        return render(request, 'lecture.html', context)
    else:
        raise Http404


def logout_user(request):
    try:
        logout(request)
        del request.session['user_id']
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('login'))


@login_required
def upload(request):
    if request.method == 'GET':
        if request.session.get('user_id', False) and request.session.get('role') != 'RO':
            courses = Course.get_courses(request.session.get('user_id'))
            context = {'courses': courses}
            return render(request, 'upload.html', context)
        else:
            return HttpResponseRedirect(reverse('login'))
    elif request.method == 'POST':
        if request.session.get('user_id', False) and request.session.get('role') != 'RO':
            lecture_form = UploadLectureForm(request.POST)
            recording = request.FILES.getlist('recording')[0]
            notes = request.FILES.getlist('notes')

            if lecture_form.is_valid():
                lecture = lecture_form.save(commit=False)
                past_lectures = Lecture.objects.filter(course=lecture.course).order_by('-index')[:1]
                if past_lectures:
                    lecture.index = past_lectures[0].index + 1
                else:
                    lecture.index = 1

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

                Notifications.new_lecture_notification(lecture)
                return HttpResponseRedirect(reverse('lecture') + '?id=' + str(lecture.id))
    else:
        raise Http404


@login_required
def post_comment(request):
    if request.method == 'POST':
        lecture_id = request.POST['lecture_id']
        comment = request.POST['comment']
        lecture = Lecture.get_lecture(lecture_id=lecture_id, user=request.user, metadata=False)

        if lecture:
            discussion = Discussion.post_comment(comment=comment, user=request.user, lecture=lecture)
            context = {
                        'comment': discussion.comment,
                        'user': "{0} {1}".format(request.user.first_name, request.user.last_name),
                        'date_created': discussion.date_created
                      }
        else:
            context = ''

        return JsonResponse(context)
