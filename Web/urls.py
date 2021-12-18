from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'Web'

urlpatterns = [
    # path('', testlist.as_view(), name='testlist'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Web/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('index/', index, name='index'),
    ]
