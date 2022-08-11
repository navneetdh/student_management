from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['roll_number', 'name', 'email']
        Widgets = {

            'roll_number': forms.TextInput(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
        }

# class StudentRegistration(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['roll_number', 'name', 'email']
#         Widgets = {
#
#             'roll_number': forms.TextInput(attrs={'class': "form-control"}),
#             'name': forms.TextInput(attrs={'class': "form-control"}),
#             'email': forms.EmailInput(attrs={'class': "form-control"}),
#         }
