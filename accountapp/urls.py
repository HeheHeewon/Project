from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp import views
from accountapp.views import signup, login_view, logout_view,sign_done

app_name="accountapp"

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signdone/', views.sign_done, name='signdone'),
    # path('mypage/', mypage, name='mypage'),
]