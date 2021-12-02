from django.db import models

# Create your models here.


class Account(models.Model):

    pid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class BicepsCurl(models.Model):
        pid = models.CharField(max_length=20)
        Lcount = models.CharField(max_length=20)
        Rcount = models.CharField(max_length=20)
        times = models.CharField(max_length=20)
        title = models.CharField(max_length=20)
        day = models.CharField(max_length=20)

    class Squat(models.Model):
        pid = models.CharField(max_length=20)
        total_time = models.CharField(max_length=20)
        count = models.IntegerField(max_length=10)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['created']

    class PushUp(models.Model):
        pid = models.CharField(max_length=20)
        total_time = models.CharField(max_length=20)
        count = models.IntegerField(max_length=10)
        created = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['created']

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "ID: "+self.pid





