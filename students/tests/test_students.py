import pytest
from random import randrange

from ..models import Student

from faker import Faker
from django.test import Client
from django.forms.models import model_to_dict


@pytest.mark.django_db
def test_student_create():
    fake = Faker()
    result = []

    for i in range(100):
        result.append(Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=randrange(1,99)
        ))
    Student.objects.bulk_create(result)

    assert Student.objects.count() == 100


def test_login():
    c = Client()
    response = c.get('')
    assert response.status_code == 200
    assert '<h2><a href="/students/">List students</a></h2>' in response.content.decode()


@pytest.mark.django_db
def test_edit_student():
    c = Client()

    generate_response = c.get('/generate_students/10')
    assert generate_response.status_code == 200
    assert Student.objects.count() == 10

    edit_response = c.post('/edit_student/1', {'first_name': 'Vitalii', 'last_name': 'Liashchenko', 'age': 25})
    assert edit_response.status_code == 200
    assert model_to_dict(Student.objects.get(pk=1)) == {'first_name': 'Vitalii', 'last_name': 'Liashchenko', 'age': 25}
