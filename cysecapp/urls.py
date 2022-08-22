from django.urls import path
from . import views

urlpatterns = [
    path('api1/user/create', views.api1_create, name='user_create'),
    path('api1/user/<int:id>', views.api1_get, name='user_get')
]
