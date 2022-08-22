from django.urls import path
from . import views

urlpatterns = [
    path('api2/user/create', views.api2_create, name='user_create'),
    path('api2/user/details', views.api2_get, name='user_get'),
    path('api2/user/login', views.api2_login, name='user_login')

]
