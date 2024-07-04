# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'  # 앱의 네임스페이스 설정

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home', views.home,name='home'),
    path('signdone', views.signdone,name='signdone'),
    path('mypage', views.mypage,name='mypage'),
    path('add_stamp', views.add_stamp,name='add_stamp'),
    path('popupreserv/<int:popup_id>/',views.popupreserv,name='popupreserv'),
]
