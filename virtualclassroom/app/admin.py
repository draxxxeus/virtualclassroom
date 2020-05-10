from django.contrib import admin
from .models import Course, Discussion, Institution, Lecture, Resource, User

admin.site.register(Course)
admin.site.register(Discussion)
admin.site.register(Institution)
admin.site.register(Lecture)
admin.site.register(Resource)
admin.site.register(User)
