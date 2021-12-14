from django.conf.urls import url
from django.urls import path
from Account import views

urlpatterns = [
    path('user-list/', views.user_list),
    path('user-login/', views.user_login),
    path('user-target/<int:pk>/', views.user_target),
    path('biceps-list/', views.biceps_list),
    path('biceps-total/', views.biceps_total),
    path('biceps-recent/', views.biceps_recent),
    path('squat-list/', views.squat_list),
    path('squat-total/', views.squat_total),
    path('squat-recent/', views.squat_recent),
    path('pushup-list/', views.squat_list),
    path('pushup-total/', views.squat_total),
    path('pushup-recent/', views.squat_recent),
    path('example/', views.example)
]