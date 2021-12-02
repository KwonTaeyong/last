from django.urls import path
from Account import views

urlpatterns = [
    path('AccountList-For-Admin/', views.AccountList),
    path('TargetAccount-Admin-For/<int:pk>/', views.Account_target),
]