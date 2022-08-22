from django.urls import path
from . import views

urlpatterns = [
    path('api8/user/create', views.api8_create, name='user_create'),
    path('api8/user/login', views.api8_login, name='user_get'),

    #path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
