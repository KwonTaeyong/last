from django.db import models

# Create your models here.


class Account(models.Model):
    pid = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)

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