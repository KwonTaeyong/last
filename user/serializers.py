from rest_framework import serializers
from .models import *


# User 모델에 대한 직렬화
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# 이두 운동 모델에 대한 직렬화
class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = '__all__'


# 스쿼트 운동 모델에 대한 직렬화
class SquatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squat
        fields = '__all__'


# 푸쉬업 운동 모델에 대한 직렬화
class PushUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushUp
        fields = '__all__'

