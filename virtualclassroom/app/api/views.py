## test mobile app login
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User


class TestView(APIView):
    """ To test if auth is working or not """
    def get(self, request):
        return Response("Tested OK! username: {}".format(request.user.username))
