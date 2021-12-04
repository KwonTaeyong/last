from django.contrib.auth.hashers import make_password
from django.db import models
from encrypted_fields import fields

# Create your models here.


class Account(models.Model):
    pid = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)

    # , null = False, default = False
    # pwd_crypted = make_password(pwd)
    # pwd = fields.EncryptedCharField(max_length=20, null=False, default=False)
    nick_name = models.CharField(max_length=40)

    created = models.DateTimeField(auto_now_add=True)
    created_str = str(created)

    def __str__(self):
        return "ID: "+self.pid

    class Meta:
        ordering = ['created']


class BicepsCurl(models.Model):
    pid = models.CharField(max_length=255)

    count = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()

    sum_times = models.IntegerField
    sum_count = models.IntegerField

    times = models.FloatField(max_length=255)
    title = models.CharField(max_length=255)

    day = models.CharField(max_length=255)
    # total_time = models.FloatField()

    # def __str__(self):
    #     return "count:"+self.Lcount+" count2:"+self.Rcount+" times:"+self.times+" title:"+self.title+" day:"+self.day

    # class Meta:
    #     ordering = ['created']


class Squat(models.Model):
    pid = models.CharField(max_length=20)
    total_time = models.CharField(max_length=20)
    count = models.IntegerField()
    # created = models.DateTimeField(auto_now_add=True)
    #
    # class Meta:
    #     ordering = ['created']


class PushUp(models.Model):
    pid = models.CharField(max_length=20)
    total_time = models.CharField(max_length=20)
    count = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class TotalNumber(models.Model):
    pid = models.CharField(max_length=20)

