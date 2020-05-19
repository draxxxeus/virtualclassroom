import uuid

from django.utils.timezone import now
from django.db import models
from datetime import datetime

from .baseModel import BaseModel
from .course import Course
import logging


logger = logging.getLogger(__name__)


class Lecture(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chapter = models.CharField(max_length=7, default=None, null=True, blank=True)  # noqa: E501
    topic = models.CharField(max_length=126, default=None, null=True, blank=True)  # noqa: E501
    index = models.PositiveIntegerField(default=1, null=False)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    publish_on = models.DateTimeField(default=now, null=True, blank=True)
    complete_by = models.DateTimeField(default=None, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def as_dict(self):
        data = dict(
            id=self.id,
            chapter=self.chapter,
            topic=self.topic,
            index=self.index,
            course=self.course.as_dict(),
            teacher=self.teacher.as_dict(),
            published_on=self.publish_on,
            complete_by=self.complete_by
        )
        return data

    @classmethod
    def get_dashboard(cls, request):
        lectures = None
        user_registration = request.user.active_registration
        if user_registration.user_role == 'RW':
            courses = Course.get_courses(user=request.user)
        elif user_registration.user_role == 'RO':
            courses = user_registration.standard.course_set.all()

        lectures = Lecture.objects.filter(course__in=courses)

        return lectures

    @classmethod
    def get_lecture(cls, request, lecture_id):
        try:
            user_registration = request.user.active_registration
            lecture = Lecture.objects.get(id=lecture_id)
            show_lecture = False

            # check if user is allowed to see the lecture
            if user_registration.user_role == 'RW':
                if lecture.course.standard.institution == user_registration.institution:  # noqa: E501
                    show_lecture = True
            elif user_registration.user_role == 'RO':
                if lecture.course in user_registration.standard.course_set.all():  # noqa: E501
                    show_lecture = True

            if show_lecture:
                resources = lecture.resource_set.all()
                prepared_lecture = {
                        'lecture': lecture,
                        'recordings': [r for r in resources if r.type == 'R'],
                        'assignments': [r for r in resources if r.type == 'A'],
                        'discussions': lecture.discussion_set.all()
                }
                return prepared_lecture
            else:
                raise
        except Exception as e:
            logger.exception("Returning None as error occurred while fetching lecture data: {}".format(e))
            return None


    @classmethod
    def get_lectures_for_course(cls, course_id):
        try:
            lectures = Lecture.objects.filter(course=course_id)
            return lectures
        except Exception as e:
            logger.exception("Returning empty like because error occurred while fetching lectures for course: {}"
                             .format(course_id))
            return []
