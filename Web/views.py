from django.http import JsonResponse, HttpResponse
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
def index(request):
    if request.method == "POST":

        form = CoverForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            title_get = data['title']
            # top_text_get = data['top_text']
            # author_get = data['author']

            if Cover.objects.filter(title=title_get).exists():
                msg = dict(
                    msg="Already Exists"
                )
                return HttpResponse("Already Exists", status=400)

            data_for_save = Cover(
                title=data['title'],
                top_text=data['top_text'],
                author=data['author'],
            )

            data_for_save.save()
            return redirect('Web:index')
    else:
        form = CoverForm()

    ctx = {
        'form': form,
    }
    return render(request, 'Web/index.html', ctx)
