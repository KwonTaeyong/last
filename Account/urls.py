from django.conf.urls import url
from django.urls import path
from Account import views

urlpatterns = [
    path('user-list/', views.user_list),
    path('user-login/', views.user_login),
    path('user-target/<int:pk>/', views.user_target),
    path('biceps-list/', views.biceps_list),
    path('biceps-total/', views.biceps_total),
    path('squat-list/', views.squat_list),
    path('squat-total/', views.squat_total),
]