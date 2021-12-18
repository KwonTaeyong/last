from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'Web'

urlpatterns = [
    path('index/', index, name='index'),
    ]
