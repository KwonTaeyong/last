from django.conf.urls import url
from django.urls import path
from Account import views

urlpatterns = [
    path('register-list/', views.register_list),
    path('user-login/', views.user_login),
    path('biceps-list/', views.BicepsList),
    path('biceps-total/', views.total_biceps),
    path('squat-list/', views.SquatList),
    # path('squat-total/', views.total_squat),
    path('TargetAccount-Admin-For/<int:pk>/', views.Account_target),
]