from django.urls import path

from . import views

app_name = 'traveling'

urlpatterns = [
    path('', views.index, name='index'),  # 첫 페이지 -> 로그인 or 회원가입 선택 가능
    path('main/', views.main, name='main'),  # 메인페이지 -> 검색을 시도할 수 있음 + 통계정보
    path('result/', views.result, name='result'),  # 결과페이지 -> 검색 결과 및 통계정보 게시
    path('detail/', views.detail, name='detail'),  # 세부페이지 -> 세부 정보 게시
    path('office/', views.office, name='office'),
]
