from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import AccountSerializer, BicepsSerializer, SquatSerializer
from .models import *


# Create your views here.
@csrf_exempt
def AccountList(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
        return HttpResponse(query_set)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)








@csrf_exempt
def Account_target(request, pk):
    try:
        target = Account.objects.get(pk=pk)
    except target.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(target)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(target, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        target.delete()
        return HttpResponse(status=204)


@csrf_exempt
def BicepsList(request):
    if request.method == 'GET':
        query_set = BicepsCurl.objects.all()
        serializer = BicepsSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
        return HttpResponse(query_set)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BicepsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def SquatList(request):
    if request.method == 'GET':
        query_set = Squat.objects.all()
        serializer = SquatSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
        return HttpResponse(query_set)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SquatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)