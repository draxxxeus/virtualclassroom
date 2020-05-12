import uuid

from django.utils.timezone import now
from django.db import models
from datetime import datetime

from .baseModel import BaseModel
from .course import Course


class Lecture(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.CharField(max_length=7, default=None, null=True, blank=True)
    topic = models.CharField(max_length=126, default=None, null=True, blank=True)
    index = models.PositiveIntegerField(default=1, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    publish_on = models.DateTimeField(default=now, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def get_lecture(cls, lecture_id, user, metadata=True):
        try:
            lecture = Lecture.objects.get(id=lecture_id)
            show_lecture = False
            if user.role != 'RO':
                show_lecture = True
            elif user.role == 'RO' and (lecture.course.standard == user.standard):
                show_lecture = True

            if show_lecture:
                if metadata:
                    resources = lecture.resource_set.all()
                    recording = [r for r in resources if r.type == 'R']
                    assignments = [r for r in resources if r.type == 'A']
                    discussions = lecture.discussion_set.all()
                    prepared_lecture = {
                            'lecture': lecture,
                            'recording': recording[0],
                            'assignments': assignments,
                            'discussions': discussions
                    }
                    return prepared_lecture
                else:
                    return lecture
            else:
                raise
        except Exception:
            return None

    @classmethod
    def get_lectures_for_user(cls, user):
        try:
            courses = Course.get_courses_for_user(user)
            if user.role == 'RW':
                lectures = Lecture.objects.filter(teacher=user).order_by('-date_created')
            else:
                lectures = Lecture.objects.filter(course__in=courses).filter(publish_on__lte=datetime.now()).filter(complete_by__gte=datetime.now()).order_by('index')

            return {'lectures': list(lectures)}
        except Exception:
            return None
