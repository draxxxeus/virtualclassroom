from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from ..models import Course, Lecture, Resource


class TestView(APIView):
    """ To test if auth is working or not """
    def get(self, request):
        return Response("Tested OK! username: {}".format(request.user.username))


class UserInfo(APIView):
    """ To handle user related requests """

    def get(self, request):
        """ Returns current user info """
        user = request.user.as_dict()
        return Response(user)


class Courses(APIView):
    """ handle course related requests """

    def get(self, request):
        """ Returns list of courses for a user """
        _courses = Course.get_courses(request.user)
        courses = [x.as_dict() for x in _courses]
        return Response(courses)


class Lectures(APIView):
    """ handles lecture related requests """

    def get(self, request):
        """ Returns lectures under a course """
        course_id = request.query_params.get('course_id')
        _lectures = Lecture.get_lectures_for_course(course_id)
        lectures = [x.as_dict() for x in _lectures]
        return Response(lectures)


class Resources(APIView):
    """ handles resource related requests """

    def get(self, request):
        lecture_id = request.query_params.get('lecture_id')
        _resources = Lecture.objects.get(id=lecture_id).resource_set.all()
        resources = [x.as_dict() for x in _resources]
        return Response(resources)


class Comments(APIView):
    """ handles comment related requests """

    def get(self, request):
        lecture_id = request.query_params.get('lecture_id')
        _comments = Lecture.objects.get(id=lecture_id).discussions_set.all()
        comments = [x.as_dict() for x in _comments]
        return Response(comments)
