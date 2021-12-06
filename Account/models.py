from django.db import models

# Create your models here.

class Account(models.Model):
    pid = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=40)

    created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return "pid: "+self.pid

    class Meta:
        ordering = ['created']


class BicepsCurl(models.Model):
    pid = models.CharField(max_length=255)

    count = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()

    sum_times = models.IntegerField
    sum_count = models.IntegerField

    times = models.FloatField(null=True, max_length=255)
    title = models.CharField(null=True, max_length=255)
    day = models.CharField(null=True, max_length=255)
    created = models.DateTimeField(null=True, auto_now_add=True)

    # def __str__(self):
    #     return "count:"+self.Lcount+" count2:"+self.Rcount+" times:"+self.times+" title:"+self.title+" day:"+self.day

    class Meta:
        ordering = ['created']


class Squat(models.Model):
    pid = models.CharField(max_length=20)

    count = models.FloatField(max_length=255)

    sum_times = models.IntegerField
    sum_count = models.IntegerField

    title = models.CharField(null=True, max_length=255)
    times = models.FloatField(null=True, max_length=255)
    day = models.CharField(null=True, max_length=255)
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created']


class PushUp(models.Model):
    pid = models.CharField(max_length=20)

    count = models.FloatField(max_length=255)

    sum_times = models.IntegerField
    sum_count = models.IntegerField

    title = models.CharField(null=True, max_length=255)
    times = models.FloatField(null=True, max_length=255)
    day = models.CharField(null=True, max_length=255)
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        ordering = ['created']