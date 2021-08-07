from django import forms

from .models import Student


# class StudentFormFromModel(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'
#         widgets = {
#             'phone': forms.TextInput()
#         }


class StudentForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Age')
    phone = forms.CharField(label='Your name', max_length=100)
