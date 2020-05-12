"""virtualclassroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lecture/post-comment/', views.post_comment, name="post_comment"),
    path('lecture/', views.lecture, name='lecture'),
    path('logout/', views.logout_user, name='logout'),
    path('upload/', views.upload, name='upload'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('switch-account/', views.switch_account, name='switch_account'),
    path('api/', include('{}.api.urls'.format(__package__))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
