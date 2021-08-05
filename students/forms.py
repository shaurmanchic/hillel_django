from django import forms

from .models import Student


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student\'s first name', max_length=200)
    last_name = forms.CharField(label='Student\'s last name', max_length=200)
    age = forms.IntegerField(label='Student\'s age')


class StudentFormFromModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']