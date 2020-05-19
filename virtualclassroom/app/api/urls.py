from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('user/', views.UserInfo.as_view(), name='user_info'),
    path('courses/', views.Courses.as_view(), name='courses_list'),  # App dashboard is populated with this.
    path('lectures/', views.Lectures.as_view(), name='course_info'),
    path('resources/', views.Resources.as_view(), name='lecture_info'),
    path('comments/', views.Comments.as_view(), name='view_video_resource')
]