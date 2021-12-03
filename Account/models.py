from django.db import models

# Create your models here.


class Account(models.Model):
    pid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    created_str = str(created)

    def __str__(self):
        return "ID: "+self.pid

    class Meta:
        ordering = ['created']


class BicepsCurl(models.Model):
    pid = models.CharField(max_length=255)
    count = models.IntegerField(max_length=255)
    count2 = models.IntegerField(max_length=255)
    times = models.FloatField(max_length=255)
    title = models.CharField(max_length=255)
    day = models.CharField(max_length=255)

    def __str__(self):
        return "count:"+self.Lcount+" count2:"+self.Rcount+" times:"+self.times+" title:"+self.title+" day:"+self.day

    # class Meta:
    #     ordering = ['created']


class Squat(models.Model):
    pid = models.CharField(max_length=20)
    total_time = models.CharField(max_length=20)
    count = models.IntegerField(max_length=10)
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









