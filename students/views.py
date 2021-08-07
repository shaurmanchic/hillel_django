# flake8: noqa
from random import randrange

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict

from faker import Faker

from .models import Student
from .forms import StudentForm


def hello(request):
    return render(request, 'index.html')


def list_students(request):
    students_list = Student.objects.all()
    return render(request, 'students_list.html', {'students': students_list})


def get_student(request, student_id):
    if request.method == 'GET':
        students_list = Student.objects.filter(id=student_id).all()
        if students_list:
            return render(request, 'students_list.html', {'students': students_list})
        else:
            return HttpResponseNotFound('No such student')
    return HttpResponse('Method not found')


def generate_students(request, student_number=100):
    fake = Faker()
    result = []

    for i in range(student_number):
        result.append(Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=randrange(1,99)
        ))
    Student.objects.bulk_create(result)

    students_list = Student.objects.all()
    return render(request, 'students_list.html', {'students': students_list})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        form = StudentForm()

    return render(request, 'student_create_form.html', {'form': form})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('list-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentForm(model_to_dict(student))

    return render(request, 'student_edit_form.html', {'form': form, 'student_id': student_id})
