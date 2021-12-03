from django.conf.urls import url
from django.urls import path
from Account import views

urlpatterns = [
    path('register-list/', views.register_list),
    path('user-login/', views.user_login),
    path('BicepsList/', views.BicepsList),
    path('SquatList/', views.SquatList),
    path('TargetAccount-Admin-For/<int:pk>/', views.Account_target),
]