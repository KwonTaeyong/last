from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django import forms

from Account.models import *
from .forms import *
from Account.models import Account
from .models import *


# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            pid_get = data['pid']
            pwd_get = data['pwd']

            try:
                target = Account.objects.get(pid=pid_get)
            except Account.DoesNotExist:
                return JsonResponse("Check ID", safe=False, status=400)

            posted_inform = Account.objects.values("pid", "pwd").get(pid=pid_get)
            posted_account = posted_inform['pid']
            posted_password = posted_inform['pwd']

            # try:
            #     target = Account.objects.get(pid=pid_get)
                # target = Account.objects.get_object_or_404(pid=pid_get)
            # except Account.DoesNotExist:
            #     return JsonResponse("Check ID", safe=False, status=400)



            if pid_get == posted_account and pwd_get == posted_password:
                return JsonResponse("Login Success", safe=False, status=200)

            if pwd_get != posted_password:
                return JsonResponse("Check PASSWORD", safe=False, status=400)

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
    return render(request, 'Web/index.html', ctx)
