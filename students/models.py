from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.phone}"
