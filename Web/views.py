from django.shortcuts import render
from django.views.generic.list import ListView
from django import forms
from Account.models import *
from .forms import RegisterForm

# Create your views here.


class testlist(ListView):
    model = BicepsCurl
    template_name = 'Web/testlist.html'


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'Web/register_done.html', {'new_user':new_user})
        else:
            user_form = RegisterForm()
    
    return render(request, 'Web/register.html', {'form':user_form})