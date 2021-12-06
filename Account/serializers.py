from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pid', 'pwd', 'nick_name', 'created']
        
        
class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = ['pid', 'count', 'count1', 'count2', 'times', 'day', 'title']


class SquatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = ['pid', 'sum_times', 'sum_count']


class BicepsTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = ['sum_times', 'sum_count']

