from random import randrange
from time import sleep

from celery import shared_task
from faker import Faker
from django.core.mail import send_mail

from .models import Student


fake = Faker()


@shared_task
def create_random_students(total):
    result = []

    for _ in range(total):
        result.append(Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=randrange(1,99)
        ))
    Student.objects.bulk_create(result)

    return '{} random students created with success!'.format(total)


@shared_task
def beat():
    print('beat START')
    sleep(5)
    print('beat END')
