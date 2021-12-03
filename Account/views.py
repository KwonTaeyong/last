from select import select

from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .serializers import AccountSerializer, BicepsSerializer, SquatSerializer
from .models import *



# Create your views here.

# 회원가입 검증 기능 및 회원리스트 보기
@csrf_exempt
def register_list(request):

    # 회원 목록을 확인하기 위함(관리자용)
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
        return HttpResponse(query_set)


    # 회원가입
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # 동일한 아이디가 존재하면 존재한다고 이야기 해주기
        if Account.objects.filter(pid=data['pid']).exists():
            msg = dict(
                msg="Already Exist ID"
            )
            return JsonResponse(msg, status=400)

        if Account.objects.filter(nick_name=data['nick_name']).exists():
            msg = dict(
                msg="Already Exists NickName"
            )

        # 동일한 아이디가 존재하지 않는다면 시리얼라이저를 통해서 가입시키기
        serializer = AccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_login(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        print(data)

        account = data['pid']
        print(account)
        print(type(account))
        password = data['pwd']
        print(password)
        print(type(password))


        list_of_PID = Account.objects.values("pid")

        posted_inform = Account.objects.values("pid", "pwd").get(pid=account)
        posted_account = posted_inform['pid']
        print(type(posted_account))
        posted_password = posted_inform['pwd']
        print(type(posted_password))

        if account == posted_account and password == posted_password:
            return JsonResponse("Login Success", safe=False, status=200)
        elif Account.objects.filter(pid=account) is None:
            return JsonResponse("Check your ID", safe=False, status=400)
        elif password != posted_password:
            return JsonResponse("Check your PASSWORD", safe=False, status=400)
    else:
        return JsonResponse("Http Method Error", safe=False, status=400)


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