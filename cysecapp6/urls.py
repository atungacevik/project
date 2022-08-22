from django.urls import path
from . import views

urlpatterns = [
    path('api6/user/create', views.api6_create, name='user_create'),
    #path('api5/user', views.api6_get_all, name='user_get'),
    path('api6/user/<int:id>', views.api6_get_by_id, name='user_get_by_id'),
    #path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
