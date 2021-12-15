from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pid', 'pwd', 'created']
        
        
class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = '__all__'
        # fields = ['pid', 'count', 'count1', 'count2', 'times', 'day', 'title', 'created']


class SquatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squat
        fields = ['pid', 'count', 'times', 'day', 'title', 'created']


class PushUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushUp
        fields = '__all__'

# 필요 없어서 주석처리
# class BicepsTotalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BicepsCurl
#         fields = ['sum_times', 'sum_count']

