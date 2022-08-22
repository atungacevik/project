from django.urls import path
from . import views

urlpatterns = [
    path('api4/user/create', views.api4_create, name='user_create'),
    path('api4/user/details', views.api4_get, name='user_get'),
    path('api4/user/login', views.api4_login, name='user_login'),
    path('api4/user/verifyOtp', views.api4_otp, name='user_otp'),
    path('api4/user/logout', views.api4_logout, name='user_logout')

]
