from django.db import models

# Create your models here.


class Account(models.Model):
    pid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "pid:"+self.pid

# 컬 운동에 대한 모델을 만든다면?
# class ExCurl(models.Model):
#     total_time = models.CharField(max_length=20)
#     rep = models.IntegerField(max_length=10)
#     count = models.IntegerField(max_length=10)
#     created = models.DateTimeField(auto_now_add=True)
#     class Meta:
#       ordering = ['created']