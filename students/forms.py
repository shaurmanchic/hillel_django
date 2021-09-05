import re

from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def phone_validator(phone):
    if not re.match(r"^380\d{9}$", phone):
        raise ValidationError(f'Invalid phone number')


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(
        label='Your name', max_length=100, validators=[phone_validator]
    )


class GenerateRandomStudentForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(500)
        ]
    )