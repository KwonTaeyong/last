from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import AccountSerializer
from .models import *

# Create your views here.

# 모든 회원 리스트 출력 및 입력
@csrf_exempt
def AccountList(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)  # 아래와 세트로
        return JsonResponse(serializer.data, safe=False)      # json형식으로 출력
        return HttpResponse(query_set)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



# 하나의 회원 정보에 접근 입출력, 수정 및 삭제
@csrf_exempt
def Account_target(request, pk):
    """
    Retrieve, update or delete a code Account.
    """
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