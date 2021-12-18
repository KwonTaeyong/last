from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.parsers import JSONParser

from .serializers import AccountSerializer, BicepsSerializer, SquatSerializer, PushUpSerializer
from .models import *


# Create your views here.
# 회원가입 검증 기능 및 회원리스트 보기
@csrf_exempt
def user_list(request):

    # 회원목록 확인
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    # 회원가입
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # 이미 존재하는 ID
        if Account.objects.filter(pid=data['pid']).exists():
            msg = dict(
                msg="Already Exists"
            )
            return JsonResponse(msg, status=400)
        # 이미 존재하는 nickName
        elif Account.objects.filter(nick_name=data['nick_name']).exists():
            msg = dict(
                msg="Already Exists NickName"
            )

        # 직렬화
        serializer = AccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_login(request):
    data = JSONParser().parse(request)
    pid_get = data['pid']
    pwd_get = data['pwd']

    try:
        target = Account.objects.get(pid=pid_get)
    except Account.DoesNotExist:
        return JsonResponse("Check your ID", safe=False, status=400)

    if request.method == 'POST':
        posted_inform = Account.objects.values("pid", "pwd").get(pid=pid_get)
        posted_account = posted_inform['pid']
        posted_password = posted_inform['pwd']

        if pid_get == posted_account and pwd_get == posted_password:
            return JsonResponse("Login Success", safe=False, status=200)

        if pwd_get != posted_password:
            return JsonResponse("Check your PASSWORD", safe=False, status=400)
    else:
        return JsonResponse("Check Request", safe=False, status=400)


@csrf_exempt
def user_target(request, pk):
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
def biceps_list(request):
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
def biceps_total(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)

        # Request를 파싱해서 pid만 뽑아내서 변수로 저장
        # account는 요청자의 pid
        pid_get = data['pid']
        result = {'Total_count': 0, 'Total_time': 0}

        # Reuqset를 파싱해서 요청받은 데이터 내용의 이름을 저장
        # 타입 필요 없이 둘을 세트로 묶을 것임
        # type_get = data['type']

        # 요청받은 데이터가 COUNT의 합계일 경우
        # if type_get == 'count':
        # if문 주석처리 했으므로 아래 sum_count부터는 1탭 만큼 앞으로
        sum_count = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('count'))
        sum_times = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('times'))

        result['Total_count'] = sum_count['count__sum']
        result['Total_time'] = sum_times['times__sum']
            # serializer = BicepsTotalSerializer(sum_count, many=True)
            # print(serializer)
        return JsonResponse(result, safe=False)

        # 요청받은 데이터가 TIMES의 합계일 경우
        # 타입 필요 없이 세트로 묶을 것이므로 일단 elif 모두 주석처리
        # elif type_get == 'times':
        #     sum_times = BicepsCurl.objects.filter(pid=pid_get).aggregate(Sum('times'))
        #     # serializer = BicepsTotalSerializer(sum_times, many=True)
        #     # print(sum_times)
        #     return JsonResponse(sum_times['times__sum'], safe=False)
    # else:
    #     return JsonResponse("Request Method Error", safe=False, status=400)


@csrf_exempt
def biceps_recent(request):

    data = JSONParser().parse(request)

    pid_get = data['pid']
    result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

    if len(BicepsCurl.objects.filter(pid=pid_get).values('count').order_by('-created')) == 0:
        result['recent_count'] = 0
    else:
        result['recent_count'] = BicepsCurl.objects.filter(pid=pid_get).values('count').order_by('-created')[0]['count']

    if len(BicepsCurl.objects.filter(pid=pid_get).values('times').order_by('-created')) == 0:
        result['recent_time'] = 0
    else:
        result['recent_time'] = BicepsCurl.objects.filter(pid=pid_get).values('times').order_by('-created')[0]['times']

    if len(BicepsCurl.objects.filter(pid=pid_get).values('day').order_by('-created')) == 0:
        result['recent_day'] = 0
    else:
        result['recent_day'] = BicepsCurl.objects.filter(pid=pid_get).values('day').order_by('-created')[0]['day']

    # data = JSONParser().parse(request)
    #
    # pid_get = data['pid']
    # result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}
    #
    # pre_count = BicepsCurl.objects.filter(pid=pid_get).values('count').order_by('-created')
    # pre_time = BicepsCurl.objects.filter(pid=pid_get).values('times').order_by('-created')
    # pre_day = BicepsCurl.objects.filter(pid=pid_get).values('day').order_by('-created')
    #
    # result['recent_count'] = pre_count[0]['count']
    # result['recent_time'] = pre_time[0]['times']
    # result['recent_day'] = pre_day[0]['day']
    #
    # serializer = BicepsSerializer(data=result)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data, status=201)

    serializer = BicepsSerializer(data=result)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(result, safe=False)


@csrf_exempt
def squat_list(request):
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
def squat_total(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)

        pid_get = data['pid']
        result = {'Total_count': 0, 'Total_time': 0}

        # try:
        #     sum_count = Squat.objects.get(pid=pid_get).aggregate(Sum('count'))
        # except Squat.DoesNotExist:
        #     result['Total_count'] = 0
        #
        # try:
        #     sum_times = Squat.objects.get(pid=pid_get).aggregate(Sum('times'))
        # except Squat.DoesNotExist:
        #     result['Total_time'] = 0

        sum_count = Squat.objects.filter(pid=pid_get).aggregate(Sum('count'))['count__sum'] or 0
        sum_times = Squat.objects.filter(pid=pid_get).aggregate(Sum('times'))['times__sum'] or 0

        result['Total_count'] = sum_count
        result['Total_time'] = sum_times

        return JsonResponse(result, safe=False)


@csrf_exempt
def squat_recent(request):

    data = JSONParser().parse(request)

    pid_get = data['pid']
    result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

    if len(Squat.objects.filter(pid=pid_get).values('count').order_by('-created')) == 0:
        result['recent_count'] = 0
    else:
        result['recent_count'] = Squat.objects.filter(pid=pid_get).values('count').order_by('-created')[0]['count']

    if len(Squat.objects.filter(pid=pid_get).values('times').order_by('-created')) == 0:
        result['recent_time'] = 0
    else:
        result['recent_time'] = Squat.objects.filter(pid=pid_get).values('times').order_by('-created')[0]['times']

    if len(Squat.objects.filter(pid=pid_get).values('day').order_by('-created')) == 0:
        result['recent_day'] = 0
    else:
        result['recent_day'] = Squat.objects.filter(pid=pid_get).values('day').order_by('-created')[0]['day']

    # pre_count = Squat.objects.filter(pid=pid_get).values('count').order_by('-created')[0]['count']
    # pre_time = Squat.objects.filter(pid=pid_get).values('times').order_by('-created') or 0
    # pre_day = Squat.objects.filter(pid=pid_get).values('day').order_by('-created') or 0

    # result['recent_count'] = pre_count[0]['count']
    # result['recent_time'] = pre_time[0]['times']
    # result['recent_day'] = pre_day[0]['day']

    # result['recent_count'] = pre_count[0]
    # result['recent_time'] = pre_time[0]
    # result['recent_day'] = pre_day[0]

    serializer = BicepsSerializer(data=result)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(result, safe=False)


@csrf_exempt
def pushup_list(request):
    if request.method == 'GET':
        query_set = PushUp.objects.all()
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
def pushup_total(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)

        pid_get = data['pid']
        result = {'Total_count': 0, 'Total_time': 0}

        try:
            sum_count = PushUp.objects.filter(pid=pid_get).aggregate(Sum('count'))
        except PushUp.DoesNotExist:
            result['Total_count'] = 0

        try:
            sum_times = PushUp.objects.filter(pid=pid_get).aggregate(Sum('times'))
        except PushUp.DoesNotExist:
            sum_times['times__sum'] = 0

        result['Total_count'] = sum_count['count__sum']
        result['Total_time'] = sum_times['times__sum']

        return JsonResponse(result, safe=False)


@csrf_exempt
def pushup_recent(request):

    data = JSONParser().parse(request)

    pid_get = data['pid']
    result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

    if len(PushUp.objects.filter(pid=pid_get).values('count').order_by('-created')) == 0:
        result['recent_count'] = 0
    else:
        result['recent_count'] = PushUp.objects.filter(pid=pid_get).values('count').order_by('-created')[0]['count']

    if len(PushUp.objects.filter(pid=pid_get).values('times').order_by('-created')) == 0:
        result['recent_time'] = 0
    else:
        result['recent_time'] = PushUp.objects.filter(pid=pid_get).values('times').order_by('-created')[0]['times']

    if len(PushUp.objects.filter(pid=pid_get).values('day').order_by('-created')) == 0:
        result['recent_day'] = 0
    else:
        result['recent_day'] = PushUp.objects.filter(pid=pid_get).values('day').order_by('-created')[0]['day']


    # data = JSONParser().parse(request)
    #
    # pid_get = data['pid']
    # result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}
    #
    # pre_count = PushUp.objects.filter(pid=pid_get).values('count').order_by('-created')
    # pre_time = PushUp.objects.filter(pid=pid_get).values('times').order_by('-created')
    # pre_day = PushUp.objects.filter(pid=pid_get).values('day').order_by('-created')
    #
    # result['recent_count'] = pre_count[0]['count']
    # result['recent_time'] = pre_time[0]['times']
    # result['recent_day'] = pre_day[0]['day']
    #
    # serializer = BicepsSerializer(data=result)
    # if serializer.is_valid():
    #     serializer.save()
    #     return JsonResponse(serializer.data)
    # else:
    #     return HttpResponse("0")

    serializer = BicepsSerializer(data=result)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(result, safe=False)


@csrf_exempt
def biceps_entire(request):
    if request.method == 'POST':
        
        data = JSONParser().parse(request)
        pid_get = data['pid']

        queryset = BicepsCurl.objects.filter(pid=pid_get).order_by('-created')

        serializer = BicepsSerializer(queryset, many=True)

        # if serializer.is_valid():
        #     serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
        # return JsonResponse(serializer.errors, status=400)

    else:
        return JsonResponse("Check Request", safe=False, status=400)


@csrf_exempt
def squat_entire(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        pid_get = data['pid']

        queryset = Squat.objects.filter(pid=pid_get).order_by('-created')

        serializer = SquatSerializer(queryset, many=True)

        # if serializer.is_valid():
        #     serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
        # return JsonResponse(serializer.errors, status=400)

    else:
        return JsonResponse("Check Request", safe=False, status=400)


@csrf_exempt
def pushup_entire(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        pid_get = data['pid']

        queryset = PushUp.objects.filter(pid=pid_get).order_by('-created')

        serializer = PushUpSerializer(queryset, many=True)

        # if serializer.is_valid():
        #     serializer.save()
        return JsonResponse(serializer.data, safe=False, status=200)
        # return JsonResponse(serializer.errors, status=400)

    else:
        return JsonResponse("Check Request", safe=False, status=400)


@csrf_exempt
def record_deleter(request):
    if request.method == 'DELETE':

        data = JSONParser().parse(request)

        pid_get = data['pid']
        day_get = data['day']
        count_get = data['count']
        exercise = data['title']

        if exercise == 'BicepsCurl':
            BicepsCurl.objects.filter(pid=pid_get).filter(count=count_get).filter(day__contains=day_get).delete()
            return HttpResponse("Successfully deleted", status=201)

        if exercise == 'Squat':
            Squat.objects.filter(pid=pid_get).filter(count=count_get).filter(day__contains=day_get).delete()
            return HttpResponse("Successfully deleted", status=201)

        if exercise == 'PushUp':
            PushUp.objects.filter(pid=pid_get).filter(count=count_get).filter(day__contains=day_get).delete()
            return HttpResponse("Successfully deleted", status=201)


        # if exercise.objects.filter(pid=pid_get).filter(day=day_get).filter(times=times_get).filter(count=count_get).exists():
        #     exercise.objects.filter(pid=pid_get).filter(day=day_get).filter(times=times_get).filter(count=count_get).delete()
        #     return JsonResponse("Successfully Done", safe=False, status=201)