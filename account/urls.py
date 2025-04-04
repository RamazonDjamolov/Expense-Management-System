from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import path

from account.views import RegisterView, LogoutView, LoginView, GoogleRegisterView, GoogleCallbackView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('Logout/', LogoutView.as_view(), name='logout'),

    # google
    path('google_register/', GoogleRegisterView.as_view(), name='google_register'),
    path('google/callback/', GoogleCallbackView.as_view(), name='google_callback'),

]
