# flake8: noqa
from random import randrange

from django.http import HttpResponse

from faker import Faker

from .models import Student


def hello(request):
    return HttpResponse("Here's the text of the Web page.")


def list_students(request):
    students_list = list(Student.objects.values().all())
    # output = '\n '.join(
    #     [f"{student.first_name} {student.last_name}, {student.age}; " for student in students_list]
    # )
    return HttpResponse(students_list)


def get_student(request):
    if request.method == 'GET':
        name_filter = request.GET.get('first_name', '')
        students_list = Student.objects.filter(first_name=name_filter).all()
        output = '\n '.join(
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
    output = [f"{student.first_name} {student.last_name}, {student.age}; \n" for student in students_list]
    return HttpResponse(output, content_type="text/plain")
