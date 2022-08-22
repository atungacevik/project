from django.urls import path
from . import views

urlpatterns = [
    path('api9/user/create', views.api9_create, name='user_create'),
    path('api9/user/v1/login', views.api9_login, name='user_get'),
    path('api9/user/v2/login', views.api9_v2_login, name='user_get'),

    #path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
