from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .import views

from accountapp.views import signup, login_view, logout_view,sign_done, my_page

app_name="accountapp"

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signdone/', views.sign_done, name='signdone'),
    path('mypage/', views.my_page, name='mypage'),
    path('mypage/add_stamp/', views.add_stamp, name='add_stamp'),
    path('mypage/verify/', views.verify, name='verify'),
    # path('accounts/', include('django.contrib.auth.urls')),  # 여기서 django.contrib.auth.urls를 include
]