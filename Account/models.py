from django.db import models
from django.contrib.auth.models import User, AbstractUser
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.


class Account(models.Model):
    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pid = models.CharField(max_length=30, null=True)
    pwd = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(null=True, auto_now_add=True)

    owner = models.ForeignKey('auth.User', related_name='Accounts', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField(null=True)

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

    # result = models.CharField(null=True, max_length=255)

    def __str__(self):
        return ("TotalCount:"+str(self.count)+" LCount:"+str(self.count1)+
                " RCount:"+str(self.count2)+" time:"+str(self.times)+" day:"+self.day)

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

    def __str__(self):
        return "Count:"+str(self.count)+" Time:"+str(self.times)+" Date:"+self.day

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

    def __str__(self):
        return "Count:"+str(self.count)+" Time:"+str(self.times)+" Date:"+self.day

    class Meta:
        ordering = ['created']


class Push(models.Model):
    pid = models.CharField(max_length=255)

    count = models.IntegerField()

    sum_times = models.IntegerField
    sum_count = models.IntegerField

    times = models.FloatField(null=True, max_length=255)
    title = models.CharField(null=True, max_length=255)
    day = models.CharField(null=True, max_length=255)
    created = models.DateTimeField(null=True, auto_now_add=True)

    # result = models.CharField(null=True, max_length=255)

    def __str__(self):
        return "TotalCount:"+str(self.count)+" time:"+str(self.times)+" day:"+self.day

    class Meta:
        ordering = ['created']


# class 아이디(AbstractUser):
#     pass


class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    # person = models.ForeignKey("Person", on_delete=models.CASCADE)


# class Person(models.Model):
#     회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.회원.username
