from django.urls import path
from . import views

urlpatterns = [
    path('api5/user/create', views.api5_create, name='user_create'),
    path('api5/users', views.api5_get_all, name='user_get'),
    path('api5/user/<int:id>', views.api5_get_by_id, name='user_get_by_id'),
    path('api5/user/<int:id>/updatePasswd', views.api5_update_passwd, name='user_update'),

]
