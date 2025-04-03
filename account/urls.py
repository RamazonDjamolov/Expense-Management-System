from django.shortcuts import render
from django.urls import path
from .views import signup, login_view, logout_view

app_name = 'account'

urlpatterns = [
    path('sign_in/', signup, name='sign_in'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    # google
]
