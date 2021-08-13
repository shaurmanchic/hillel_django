from django import forms

from django.core.validators import MinValueValidator, MaxValueValidator


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(label='Your name', max_length=100)


class GenerateRandomStudentForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )