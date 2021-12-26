from django.urls import path
from django.contrib.auth import views as auth_views
from Web import views

urlpatterns = [
    path('exlogin/', views.exlogin, name='exlogin'),
    # path('main', views.render_login, name='render_login'),
    # path('perform_login', views.perform_login, name='perform_login'),
    # path('perform_logout', views.perform_logout, name='perform_logout'),
    # path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # path('home/', views.home, name='home'),
    # path('create/', views.Create.as_view(), name='create'),
    path('join/', views.exjoin, name='join'),
    path('delete/', views.exdelete, name='delete'),
    path('performjoin/', views.perform_join, name='performjoin'),
    path('performdelete/', views.perform_delete, name='performdelete'),
    path('introduce/', views.introduce, name='introduce'),
    path('index/', views.index, name='index'),
 ]
