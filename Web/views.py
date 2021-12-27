from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from django import forms

from user.models import *
from user.models import *
from .models import *
from .forms import *



def exlogin(request):
    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            username_get = data['username']
            password_get = data['password']

            try:
                target = User.objects.get(username=username_get)
            except User.DoesNotExist:
                return render(request, 'Web/error.html', {'err': 0})

            posted_inform = User.objects.values("username", "password").get(username=username_get)
            posted_account = posted_inform['username']
            posted_password = posted_inform['password']

            if username_get == posted_account and password_get == posted_password:
                biceps_queryset = BicepsCurl.objects.filter(username=username_get)
                squat_queryset = Squat.objects.filter(username=username_get)
                pushup_queryset = PushUp.objects.filter(username=password_get)
                context = {
                    'username': username_get,
                    'biceps_queryset': biceps_queryset,
                    'squat_queryset': squat_queryset,
                    'pushup_queryset': pushup_queryset,
                }
                return render(request, 'Web/main.html', context)

            if password_get != posted_password:
                return render(request, 'Web/error.html', {'err': 1})

    else:
        form = LoginForm()

        ctx = {
            'form': form,
        }
    return render(request, 'Web/exlogin.html', ctx)


def exjoin(request):
    form = JoinForm()
    context = {
        'form': form
    }
    return render(request, 'Web/join.html', context)


def exdelete(request):
    form = DeleteForm()
    context = {
        'form': form
    }
    return render(request, 'Web/delete.html', context)


def perform_join(request):
    if request.method == "POST":

        form = JoinForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            username_get = data['username']
            password_get = data['password']

            if User.objects.filter(username=username_get).exists():
                return render(request, 'Web/error.html', {'err': 3})

            else:
                user = User()
                user.username = username_get
                user.password = password_get
                user.save()

                return redirect('exlogin')

        form = JoinForm()

        ctx = {
            'form': form,
        }
    return render(request, 'Web/join.html', ctx)


def perform_delete(request):
    if request.method == "POST":

        form = DeleteForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            username_get = data['username']
            password_get = data['password']

            try:
                posted_inform = User.objects.values("username", "password").get(username=username_get)
                posted_account = posted_inform['username']
                posted_password = posted_inform['password']

                if username_get == posted_account and password_get == posted_password:
                    User.objects.filter(password=password_get).get(username=username_get).delete()
                    User.objects.get(username=username_get).delete()

                    return redirect('exlogin')

            except User.DoesNotExist:
                return redirect('exlogin')

   
def index(request):
    form = LoginForm()

    ctx = {
            'form': form,
        }
    return render(request, 'Web/index.html', ctx)


def introduce(request):
    return render(request, 'Web/introduce.html')
