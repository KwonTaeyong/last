from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# AbstractUser 상속 / setting.py에 AUTH_USER_MODEL = '앱이름.클래스이름' 써줘야 한다
class User(AbstractUser, PermissionsMixin):
    class Meta:
        ordering = ['date_joined']

    ## AbstractUser에 정의되어 있으나 본 프로젝트에서는 사용하지 않을 것임
    ## 이렇게까지 해서 AbstractUser를 상속받는 이유? django에서 제공하는 security관련 기능을 보장받기 위해서
    # username = models.CharField()
    # password = models.CharField()
    # last_login = models.DateTimeField(blank=True, null=True)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=150, blank=True)
    # email = models.EmailField(blank=True)
    # is_staff = models.BooleanField()
    # is_active = models.BooleanField()
    # date_joined = models.DateTimeField()
    # is_superuser = models.BooleanField()


# 이두 운동 관련된 모델
class BicepsCurl(models.Model):
    # User 모델의 정보를 상속하기 위해서 / 상단에 기입해야할 것 : from django.conf import settings
    username = models.CharField(max_length=25)

    count = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()

    sum_times = models.IntegerField(null=True)
    sum_count = models.IntegerField(null=True)

    times = models.FloatField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    day = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("TotalCount:"+str(self.count)+" LCount:"+str(self.count1)+
                " RCount:"+str(self.count2)+" time:"+str(self.times)+" day:"+self.day)

    class Meta:
        ordering = ['created']


# 스쿼트 운동 관련 모델
class Squat(models.Model):
    username = models.CharField(max_length=25)

    count = models.FloatField(max_length=255)

    sum_times = models.IntegerField(null=True)
    sum_count = models.IntegerField(null=True)

    times = models.FloatField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    day = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Count:"+str(self.count)+" Time:"+str(self.times)+" Date:"+self.day

    class Meta:
        ordering = ['created']


# 푸쉬업 운동 관련 모델
class PushUp(models.Model):
    username = models.CharField(max_length=25)

    count = models.FloatField(max_length=255)

    sum_times = models.IntegerField(null=True)
    sum_count = models.IntegerField(null=True)

    times = models.FloatField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    day = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Count:"+str(self.count)+" Time:"+str(self.times)+" Date:"+self.day

    class Meta:
        ordering = ['created']