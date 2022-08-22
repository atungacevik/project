from django.urls import path
from . import views

urlpatterns = [
    path('api7/user/create', views.api7_create, name='user_create'),
    path('api7/user/login', views.api7_login, name='user_get'),
    path('api7/user/<int:id>', views.api7_get_by_id, name='user_get_by_id'),
    path('api7/user/login/auth_token', views.api7_auth_token, name='user_get_token'),

    #path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
