from django.shortcuts import render
from django.urls import path
from .views import LoginView, LogoutView, RegisterView

app_name = 'account'

urlpatterns = [
    path('sign_in/', RegisterView.as_view(), name='sign_in'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # google


]
