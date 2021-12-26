from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from user import views

urlpatterns = [
    # 회원리스트 / 로그인 / 개인조회
    path('user-list/', views.user_list),
    path('user-login/', views.user_login),
    path('user-target/<int:pk>/', views.user_target),

    # 이두 운동 / 총 정보 / 필터: 총 횟수, 최근기록, 한 줄 기록 / 한 줄 기록에는 DELETE 요청 가능
    path('biceps-list/', views.biceps_list),
    path('biceps-list/total', views.biceps_total),
    path('biceps-list/recent', views.biceps_recent),
    path('biceps-list/entire/', views.biceps_entire),

    # 스쿼트 운동 / 총 정보 / 필터: 총 횟수, 최근기록, 한 줄 기록 / 한 줄 기록에는 DELETE 요청 가능
    path('squat-list/', views.squat_list),
    path('squat-list/total', views.squat_total),
    path('squat-list/recent', views.squat_recent),
    path('squat-list/entire/', views.squat_entire),

    # 푸쉬업 운동 / 총 정보 / 필터: 총 횟수, 최근기록, 한 줄 기록 / 한 줄 기록에는 DELETE 요청 가능
    path('pushup-list/', views.pushup_list),
    path('pushup-list/total', views.pushup_total),
    path('pushup-list/recent', views.pushup_recent),
    path('pushup-list/entire/', views.pushup_entire),

    # (구) 한 줄 기록 삭제하기 / 필터: 운동이름
    # path('record-del/', views.record_deleter),
]

# 다른 포맷의 언어 등에 대응력을 갖추기 위한 포맷팅 코드
urlpatterns = format_suffix_patterns(urlpatterns)

