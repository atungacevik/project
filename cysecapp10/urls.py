from django.urls import path
from . import views

urlpatterns = [
    path('api10/user/create', views.api10_create, name='user_create'),
    path('api10/user/login', views.api7_login, name='user_get'),


    #path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
