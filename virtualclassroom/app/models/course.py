import uuid

from django.db import models

from .baseModel import BaseModel


def get_textbook_path(instance, filename):
    return 'courses/{0}/{1}'.format(instance.id, filename)


class Course(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=30)
    standard = models.ForeignKey('Standard', on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=14, default=None, null=True, blank=True)  # noqa: E501
    textbook = models.FileField(upload_to=get_textbook_path, null=True, blank=True)  # noqa: E501
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    @classmethod
    def get_courses(cls, user):
        user_registration = user.active_registration
        if user_registration.user_role == 'RW':
            standard = user_registration.institution.standard_set.all()
            courses = Course.objects.filter(teacher=user, standard__in=standard)  # noqa:E501
        elif user_registration.user_role == 'RO':
            courses = user_registration.standard.course_set.all()

        return courses
