from django.urls import path
from Account import views

urlpatterns = [
    path('AccountList-For-Admin/', views.AccountList),
    path('BicepsList/', views.BicepsList),
    path('TargetAccount-Admin-For/<int:pk>/', views.Account_target),
]