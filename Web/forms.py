from django.contrib.auth.models import User
from django import forms
from user.models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='ID')
    password = forms.CharField(widget=forms.PasswordInput, label='PW')


class JoinForm(forms.Form):
    username = forms.CharField(label='ID')
    password = forms.CharField(widget=forms.PasswordInput, label='PW')


class DeleteForm(forms.Form):
    username = forms.CharField(label='ID')
    password = forms.CharField(widget=forms.PasswordInput, label='PW')


