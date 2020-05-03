from django.contrib import admin
from .models import Course, Lecture, Resource, School, User

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Resource)
admin.site.register(School)
admin.site.register(User)
