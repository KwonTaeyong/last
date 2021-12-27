from django.http import HttpResponse, JsonResponse
from django.db.models import Sum
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, BicepsSerializer, SquatSerializer, PushUpSerializer
from .models import *


# 회원가입 & 회원리스트 / 등록 조회
@api_view(['GET', 'POST'])
def user_list(request):
    # 회원목록 확인
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        print("회원목록 출력 완료")
        return JsonResponse(serializer.data, safe=False)
    # 회원가입
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # 이미 존재하는 ID
        if User.objects.filter(username=data['username']).exists():
            msg = dict(
                msg="Already Exists"
            )
            return JsonResponse(msg, status=400)
        # 직렬화 및 유효성 검사 후 저장
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("회원가입 완료")
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# 로그인 검증
@api_view(['POST'])
def user_login(request):
    data = JSONParser().parse(request)
    username_get = data['username']
    password_get = data['password']

    try:
        target = User.objects.get(username=username_get)
    except User.DoesNotExist:
        return JsonResponse("Check your ID", safe=False, status=400)

    if request.method == 'POST':
        posted_inform = User.objects.values("username", "password").get(username=username_get)
        posted_account = posted_inform['username']
        posted_password = posted_inform['password']

        if username_get == posted_account and password_get == posted_password:
            print("Successfully Logged: "+username_get)
            return JsonResponse("Login Success", safe=False, status=200)

        if password_get != posted_password:
            print("Logged not allowed/wrong password: "+username_get)
            return JsonResponse("Check your PASSWORD", safe=False, status=400)
    else:
        print("Wrong Access: Not allowed Method")
        return JsonResponse("Check Request", safe=False, status=400)


# 유저 한명한명 / 조회 / 필요성 아직 못 느낌
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_target(request, pk):
    try:
        target = User.objects.get(pk=pk)
    except target.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(target)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(target, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        target.delete()
        return HttpResponse(status=204)


# 이두 운동 모든 기록 / 조회 등록
@api_view(['GET', 'POST'])
def biceps_list(request):
    if request.method == 'GET':
        query_set = BicepsCurl.objects.all()
        serializer = BicepsSerializer(query_set, many=True)
        print("GET BicepsList: OK")
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BicepsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("POST BicepsList: OK")
            return JsonResponse(serializer.data, status=201)
        print("Err occurs: Serializer")
        return JsonResponse(serializer.errors, status=400)


# 이두 운동 총 횟수 및 시간 / 조회
@api_view(['POST'])
def biceps_total(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'Total_count': 0, 'Total_time': 0}

        sum_count = BicepsCurl.objects.filter(username=username_get).aggregate(Sum('count'))
        sum_times = BicepsCurl.objects.filter(username=username_get).aggregate(Sum('times'))

        result['Total_count'] = sum_count['count__sum']
        result['Total_time'] = sum_times['times__sum']
        print("GET by post Biceps TOTAL COUNT&TIME: OK")
        return JsonResponse(result, safe=False)


# 이두 최근 기록 / 조회
@api_view(['POST'])
def biceps_recent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

        if len(BicepsCurl.objects.filter(username=username_get).values('count').order_by('-created')) == 0:
            result['recent_count'] = 0
        else:
            result['recent_count'] = BicepsCurl.objects.filter(username=username_get).values('count').order_by('-created')[0]['count']

        if len(BicepsCurl.objects.filter(username=username_get).values('times').order_by('-created')) == 0:
            result['recent_time'] = 0
        else:
            result['recent_time'] = BicepsCurl.objects.filter(username=username_get).values('times').order_by('-created')[0]['times']

        if len(BicepsCurl.objects.filter(username=username_get).values('day').order_by('-created')) == 0:
            result['recent_day'] = 0
        else:
            result['recent_day'] = BicepsCurl.objects.filter(username=username_get).values('day').order_by('-created')[0]['day']

        serializer = BicepsSerializer(data=result)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        print("GET by post Biceps RECENT: OK")
        return JsonResponse(result, safe=False)


# 스쿼트 운동 모든 기록 / 조회 등록
@api_view(['GET', 'POST'])
def squat_list(request):
    if request.method == 'GET':
        query_set = Squat.objects.all()
        serializer = SquatSerializer(query_set, many=True)
        print("GET SquatList: OK")
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SquatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("POST SquatList: OK")
            return JsonResponse(serializer.data, status=201)
        print("Err occurs: Serializer")
        return JsonResponse(serializer.errors, status=400)


# 스쿼트 운동 총 횟수 및 시간 / 조회
@api_view(['POST'])
def squat_total(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'Total_count': 0, 'Total_time': 0}

        sum_count = Squat.objects.filter(username=username_get).aggregate(Sum('count'))['count__sum'] or 0
        sum_times = Squat.objects.filter(username=username_get).aggregate(Sum('times'))['times__sum'] or 0

        result['Total_count'] = sum_count
        result['Total_time'] = sum_times
        print("GET by post Squat TOTAL COUNT&TIME: OK")
        return JsonResponse(result, safe=False)


# 스쿼트 운동 최근 기록 / 조회
@api_view(['POST'])
def squat_recent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

        if len(Squat.objects.filter(username=username_get).values('count').order_by('-created')) == 0:
            result['recent_count'] = 0
        else:
            result['recent_count'] = Squat.objects.filter(username=username_get).values('count').order_by('-created')[0]['count']

        if len(Squat.objects.filter(username=username_get).values('times').order_by('-created')) == 0:
            result['recent_time'] = 0
        else:
            result['recent_time'] = Squat.objects.filter(username=username_get).values('times').order_by('-created')[0]['times']

        if len(Squat.objects.filter(username=username_get).values('day').order_by('-created')) == 0:
            result['recent_day'] = 0
        else:
            result['recent_day'] = Squat.objects.filter(username=username_get).values('day').order_by('-created')[0]['day']

        serializer = BicepsSerializer(data=result)

        if serializer.is_valid():
            serializer.save()
            print("GET by post Biceps RECENT: OK")
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(result, safe=False)


# 푸쉬업 운동 모든 기록 / 조희 등록
@api_view(['GET', 'POST'])
def pushup_list(request):
    if request.method == 'GET':
        query_set = PushUp.objects.all()
        serializer = PushUpSerializer(query_set, many=True)
        print("GET PushUpList: OK")
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PushUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("POST PushUpList: OK")
            return JsonResponse(serializer.data, status=201)
        print("Err occurs: Serializer")
        return JsonResponse(serializer.errors, status=400)


# 푸쉬업 운동 총 횟수 및 시간 / 조회
@api_view(['POST'])
def pushup_total(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'Total_count': 0, 'Total_time': 0}

        try:
            sum_count = PushUp.objects.filter(username=username_get).aggregate(Sum('count'))
        except PushUp.DoesNotExist:
            result['Total_count'] = 0

        try:
            sum_times = PushUp.objects.filter(username=username_get).aggregate(Sum('times'))
        except PushUp.DoesNotExist:
            sum_times['times__sum'] = 0

        result['Total_count'] = sum_count['count__sum']
        result['Total_time'] = sum_times['times__sum']
        print("GET by post PushUp TOTAL COUNT&TIME: OK")
        return JsonResponse(result, safe=False)


# 푸쉬업 운동 최근 기록 / 조회
@api_view(['POST'])
def pushup_recent(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        username_get = data['username']
        result = {'recent_count': 0, 'recent_time': 0, 'recent_day': 0}

        if len(PushUp.objects.filter(username=username_get).values('count').order_by('-created')) == 0:
            result['recent_count'] = 0
        else:
            result['recent_count'] = PushUp.objects.filter(username=username_get).values('count').order_by('-created')[0]['count']

        if len(PushUp.objects.filter(username=username_get).values('times').order_by('-created')) == 0:
            result['recent_time'] = 0
        else:
            result['recent_time'] = PushUp.objects.filter(username=username_get).values('times').order_by('-created')[0]['times']

        if len(PushUp.objects.filter(username=username_get).values('day').order_by('-created')) == 0:
            result['recent_day'] = 0
        else:
            result['recent_day'] = PushUp.objects.filter(username=username_get).values('day').order_by('-created')[0]['day']

        serializer = BicepsSerializer(data=result)

        if serializer.is_valid():
            serializer.save()
            print("GET by post PushUp RECENT: OK")
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(result, safe=False)


# 이두 운동 한 줄 정보 / 조회 삭제
@api_view(['POST', 'DELETE'])
def biceps_entire(request):
    data = JSONParser().parse(request)

    if request.method == 'POST':
        username_get = data['username']

        queryset = BicepsCurl.objects.filter(username=username_get).order_by('-created')
        serializer = BicepsSerializer(queryset, many=True)
        print("GET by post Biceps ALL RECORD ORDERED: OK")
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'DELETE':
        username_get = data['username']
        day_get = data['day']
        count_get = data['count']

        BicepsCurl.objects.filter(username=username_get).filter(count=count_get).filter(day__contains=day_get).delete()
        print("DELETE Biceps RECORD ORDERED: OK")
        return HttpResponse("Successfully deleted", status=201)

    else:
        return JsonResponse("Check Request", safe=False, status=400)


# 스쿼트 운동 한 줄 정보 / 조회 삭제
@api_view(['POST', 'DELETE'])
def squat_entire(request):
    data = JSONParser().parse(request)

    if request.method == 'POST':
        username_get = data['username']

        queryset = Squat.objects.filter(username=username_get).order_by('-created')
        serializer = SquatSerializer(queryset, many=True)
        print("GET by post Squat ALL RECORD ORDERED: OK")
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'DELETE':
        username_get = data['username']
        day_get = data['day']
        count_get = data['count']

        Squat.objects.filter(username=username_get).filter(count=count_get).filter(day__contains=day_get).delete()
        print("DELETE Squat RECORD ORDERED: OK")
        return HttpResponse("Successfully deleted", status=201)

    else:
        return JsonResponse("Check Request", safe=False, status=400)


# 푸쉬업 운동 한 줄 정보 / 조회 삭제
@api_view(['POST', 'DELETE'])
def pushup_entire(request):
    data = JSONParser().parse(request)

    if request.method == 'POST':
        username_get = data['username']

        queryset = PushUp.objects.filter(username=username_get).order_by('-created')
        serializer = PushUpSerializer(queryset, many=True)
        print("GET by post PushUp ALL RECORD ORDERED: OK")
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'DELETE':
        username_get = data['username']
        day_get = data['day']
        count_get = data['count']

        PushUp.objects.filter(username=username_get).filter(count=count_get).filter(day__contains=day_get).delete()
        print("DELETE PushUp RECORD ORDERED: OK")
        return HttpResponse("Successfully deleted", status=201)

    else:
        return JsonResponse("Check Request", safe=False, status=400)