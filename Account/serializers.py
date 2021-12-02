from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['pid', 'pwd', 'created']
        
        
class BicepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account.BicepsCurl
        fields = ['pid', 'Rcount', 'Lcount', 'times', 'day', 'title']



