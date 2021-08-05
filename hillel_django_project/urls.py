"""hillel_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from students.views import (
    hello,
    list_students,
    get_student,
    generate_students,
    create_student,
    create_student_from_model
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('list_students/', list_students),
    path('get_student', get_student),
    path('generate_students/<int:student_number>', generate_students),
    path('create_student', create_student),
    path('create_student_from_model', create_student_from_model),
]
