from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.db.models import Sum

from rest_framework.parsers import JSONParser

from .serializers import AccountSerializer, BicepsSerializer, SquatSerializer, BicepsTotalSerializer
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
        print(list_of_PID)

        # posted_inform = Account.objects.values("pid", "pwd").get(pid=account)
        posted_inform = Account.objects.values("pid", "pwd").get(pid=account)
        print(type(posted_inform))
        posted_account = posted_inform['pid']
        print(type(posted_account))
        posted_password = posted_inform['pwd']
        print(type(posted_password))

        try:
            target = Account.objects.get(pid=account)
        except target.DoesNotExist:
            return HttpResponse("Check your ID", status=400)

        if account == posted_account and password == posted_password:
            return JsonResponse("Login Success", safe=False, status=200)

        if password != posted_password:
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
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SquatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def total_biceps(request):
    if request.method == 'GET':

        data = JSONParser().parse(request)
        print(data)
        # Request를 파싱해서 pid만 뽑아내서 변수로 저장
        # account는 요청자의 pid
        pid_get = data['pid']
        print(pid_get)
        # Reuqset를 파싱해서 요청받은 데이터 내용의 이름을 저장
        type_get = data['type']
        print(type_get)
        # 요청받은 데이터가 COUNT의 합계일 경우
        if type_get == 'count':
            sum_count = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('count'))
            print(sum_count)
            # serializer = BicepsTotalSerializer(sum_count, many=True)
            # print(serializer)
            return JsonResponse(sum_count['count__sum'], safe=False)
        # 요청받은 데이터가 TIMES의 합계일 경우
        elif type_get == 'times':
            sum_times = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('times'))
            print(sum_times)
            # serializer = BicepsTotalSerializer(sum_times, many=True)
            # print(sum_times)
            return JsonResponse(sum_times['times__sum'], safe=False)

        # # ORM으로 요청자의 BicepsCurl 정보를 찾아온다
        # sum_count = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('count'))
        # sum_times = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('times'))
        #
        # dict_sum = {}
        # dict_sum['sum_count'] = sum_count
        # dict_sum['sum_times'] = sum_times
        #
        # # serializer에 넣고 돌린다 (??)
        # serializer = TotalNumberSerializer(dict_sum, many=True)
        # return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse("Http Method Error", safe=False, status=400)

