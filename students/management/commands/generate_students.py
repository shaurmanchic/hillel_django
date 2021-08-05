from random import randrange

from django.core.management.base import BaseCommand, CommandError
from students.models import Student

from faker import Faker

class Command(BaseCommand):
    help = 'Genereates random students base on input amount'

    def add_arguments(self, parser):
        parser.add_argument('number_of_students', nargs='?', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        result = []

        for i in range(options['number_of_students']):
            result.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randrange(1,99)
            ))
        Student.objects.bulk_create(result)

        self.stdout.write(self.style.SUCCESS('Successfully created students'))