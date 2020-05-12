from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('user/', views.UserRecordView.as_view(), name='user')
]