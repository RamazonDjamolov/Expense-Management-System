from django.shortcuts import render
from django.urls import path
from .views import google_login, google_callback, signup, login_view, logout_view

app_name = 'account'

urlpatterns = [
    path('sign_in/', signup, name='sign_in'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    # google
    path('google_login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
]
