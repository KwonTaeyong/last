from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django import forms

from Account.models import *
from .forms import *
from Account.models import Account
from .models import *


@csrf_exempt
def exlogin(request):
    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            pid_get = data['pid']
            pwd_get = data['pwd']

            try:
                target = Account.objects.get(pid=pid_get)
            except Account.DoesNotExist:
                # return JsonResponse("Check ID", safe=False, status=400)
                return render(request, 'Web/error.html', {'err': 0})

            posted_inform = Account.objects.values("pid", "pwd").get(pid=pid_get)
            posted_account = posted_inform['pid']
            posted_password = posted_inform['pwd']

            if pid_get == posted_account and pwd_get == posted_password:
                biceps_queryset = BicepsCurl.objects.filter(pid=pid_get)
                squat_queryset = Squat.objects.filter(pid=pid_get)
                pushup_queryset = PushUp.objects.filter(pid=pid_get)
                context = {
                    'pid': pid_get,
                    'biceps_queryset': biceps_queryset,
                    'squat_queryset': squat_queryset,
                    'pushup_queryset': pushup_queryset,
                }
                return render(request, 'Web/main.html', context)

            if pwd_get != posted_password:
                # return JsonResponse("Check PASSWORD", safe=False, status=400)
                return render(request, 'Web/error.html', {'err': 1})

            # top_text_get = data['top_text']
            # author_get = data['author']

            # This is not for LOGIN but REGISTER
            # if Account.objects.filter(pid=pid_get).exists():
            #     msg = dict(
            #         msg="Already Exists"
            #     )
            #     return HttpResponse("Already Exists", status=400)
            #
            # data_for_save = Account(
            #     pid=data['pid'],
            #     pwd=data['pwd'],
            # )
            #
            # data_for_save.save()
            # return redirect('Web:index')
    else:
        form = LoginForm()

        ctx = {
            'form': form,
        }
    return render(request, 'Web/exlogin.html', ctx)


# @csrf_exempt
# def login(request):
#     return render(request, 'Web/login.html')


# def render_login(request):
#     return render(request, 'Web/login.html')


# def perform_login(request):
#     if request.method != 'POST':
#         return HttpResponse("Not allowed method")
#     else:
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user_obj = authenticate(request, pid=username, pwd=password)
#         if user_obj is not None:
#             login(request, user_obj)
#             return HttpResponseRedirect("admin_dashboard")
#         else:
#             return HttpResponseRedirect(reverse('render_login'))


# def admin_dashboard(request):
#     return render(request, "Web/admin_dashboard.html")
#
#
# def perform_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('render_login'))


# def textlist(request):
#     pid_get = request.data['pid']
#     queryset = BicepsCurl.objects.filter(pid=pid_get)
#     context = {
#         'queryset': queryset,
#     }
#     return render(request, 'Web/main.html')


# def home(request):
#     context = {
#         "메뉴명": "자장면",
#         "가격": "700원"
#     }
#     return render(request, "아무거나2.html", context)


# class Create(CreateView):
#     model = Account
#     fields = ['pid', 'pwd']
#     success_url = reverse_lazy('exlogin')
#     template_name = 'Web/join.html'


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


@csrf_exempt
def perform_join(request):
    if request.method == "POST":

        form = JoinForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            pid_get = data['pid']
            pwd_get = data['pwd']

            if Account.objects.filter(pid=pid_get).exists():
                return render(request, 'Web/error.html', {'err': 3})

            else:
                user = Account()
                user.pid = pid_get
                user.pwd = pwd_get
                user.save()

                # form = LoginForm()
                #
                # ctx = {
                #     'form': form,
                # }
                return redirect('exlogin')
                # return render(request, 'Web/exlogin.html', ctx)

            form = JoinForm()

            ctx = {
                'form': form,
            }
    return render(request, 'Web/join.html', ctx)


@csrf_exempt
def perform_delete(request):
    if request.method == "POST":

        form = DeleteForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            pid_get = data['pid']
            pwd_get = data['pwd']

            try:
                posted_inform = Account.objects.values("pid", "pwd").get(pid=pid_get)
                posted_account = posted_inform['pid']
                posted_password = posted_inform['pwd']

                if pid_get == posted_account and pwd_get == posted_password:
                    # BicepsCurl.objects.get(pid=pid_get).delete()
                    # Squat.objects.get(pid=pid_get).delete()
                    # PushUp.objects.get(pid=pid_get).delete()
                    Account.objects.filter(pwd=pwd_get).get(pid=pid_get).delete()
                    Account.objects.get(pid=pid_get).delete()

                    return redirect('exlogin')

            except Account.DoesNotExist:
                return redirect('exlogin')

    
def index(request):
    form = LoginForm()

    ctx = {
            'form': form,
        }
    return render(request, 'Web/index.html', ctx)

def introduce(request):
    return render(request, 'Web/introduce.html')