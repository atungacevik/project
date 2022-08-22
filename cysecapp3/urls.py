from django.urls import path
from . import views

urlpatterns = [
    path('api3/user/create', views.api3_create, name='user_create'),
    path('api3/user/comment', views.api3_create_comment, name='user_comment_create'),
    path('api3/user/get/comments', views.api3_get_comments, name='user_get_comments'),
    path('api3/user/verifyOtp', views.api3_otp, name='user_otp'),
    path('api3/user/logout', views.api3_logout, name='user_logout')

]
