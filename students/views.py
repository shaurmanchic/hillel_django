# flake8: noqa
from random import randrange

from django.http import HttpResponse
from django.shortcuts import render

from faker import Faker

from .models import Student
from .forms import StudentForm, StudentFormFromModel


def hello(request):
    return HttpResponse("Here's the text of the Web page.")


def list_students(request):
    students_list = Student.objects.all()
    output = '<br> '.join(
        [f"{student.first_name} {student.last_name}, {student.age}; " for student in students_list]
    )
    return HttpResponse(output)


def get_student(request):
    if request.method == 'GET':
        name_filter = request.GET.get('first_name', '')
        students_list = Student.objects.filter(first_name=name_filter).all()
        output = '<br> '.join(
            [f"{student.first_name} {student.last_name}, {student.age}; " for student in students_list]
        )
        return HttpResponse(output)
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
    output = [f"{student.first_name} {student.last_name}, {student.age}; " for student in students_list]
    return HttpResponse(output, content_type="text/plain")


def create_student(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('Student created!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'student.html', {'form': form})


def create_student_from_model(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentFormFromModel(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('Student created!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentFormFromModel()

    return render(request, 'student_from_model.html', {'form': form})
