from django.contrib.auth.models import User
from django import forms
from Account.models import *


class LoginForm(forms.Form):
    pid = forms.CharField()
    pwd = forms.CharField()
    

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Check Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         fields = ['pid', 'pwd']
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords not matched')
#         return cd['password2']
