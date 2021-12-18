from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django import forms
from Account.models import *
from .forms import *
from .models import *

from .serializers import CoverSerializer

# Create your views here.


@csrf_exempt
class testlist(ListView):
    model = BicepsCurl
    template_name = 'Web/testlist.html'


@csrf_exempt
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


@csrf_exempt
def create(request):
    user = User()
    user.name = request.POST.get('Name')
    user.phone = request.POST.get('Phone')
    user.email = request.POST.get('Email')
    user.save()
    print(user)

    return redirect('/')

@csrf_exempt
def index(request):
    if request.method == "POST":

        form = CoverForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            pc = Cover(
                title=cd['title'],
                top_text=cd['top_text'],
                author=cd['author'],
            )

            pc.save()
            return redirect('Web:index')
    else:
        form = CoverForm()

    ctx = {
        'form': form,
    }
    return render(request, 'Web/index.html', ctx)
