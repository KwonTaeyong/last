from django.db import models

# Create your models here.


class Cover(models.Model):
    title = models.CharField(max_length=20)
    top_text = models.CharField(max_length=20)
    author = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "title:"+self.title+"/ top_text:"+self.top_text+"/ author:"+self.author
