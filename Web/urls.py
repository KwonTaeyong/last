from django.urls import path
from django.contrib.auth import views as auth_views
from Web import views

urlpatterns = [
    path('exlogin/', views.exlogin, name='exlogin'),
    path('join/', views.exjoin, name='join'),
    path('delete/', views.exdelete, name='delete'),
    path('performjoin/', views.perform_join, name='performjoin'),
    path('performdelete/', views.perform_delete, name='performdelete'),
    path('introduce/', views.introduce, name='introduce'),
    path('index/', views.index, name='index'),
 ]
