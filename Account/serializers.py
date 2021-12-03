from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pid', 'pwd', 'nick_name', 'created']
        
        
class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = ['pid', 'count', 'count2', 'times', 'day', 'title']

class SquatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicepsCurl
        fields = ['pid', 'total_time', 'count']



