from django.urls import path
from . import views
from .views import mypage

app_name='popplace'

urlpatterns = [
  path('', views.splash, name='splash'),
  path('main/', views.main, name='main'),
  path('search/', views.search, name='search'),
  path('map/', views.map, name='map'),
  path('magazine/', views.magazine, name='magazine'),
  path('mypage/', views.mypage, name='mypage'),
  path('account/login/', views.login, name='login'),
  path('signup/', views.signup, name='signup'),
  path('signup/done', views.signdone, name='signdone'),
  path('popupstore/', views.popupstore, name='popupstores'),
  path('popupstore/<int:popup_id>/', views.popupstore, name='popupstore'),
  path('popupstore/<int:popup_id>/reservation', views.popupreserv, name='popupreserv'),
  path('popupstore/<int:popup_id>/reserved',views.popupreserved, name='popupreserved'),
  path('popupstore/<int:popup_id>/review', views.popupreview, name='popupreview'),
  path('mypage/reservation_history/', views.reservation_history, name='reservation_history'),
  
]