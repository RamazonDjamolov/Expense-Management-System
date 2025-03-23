from django.shortcuts import render
from django.urls import path
from .views import google_login, google_callback, sign_in

app_name = 'account'

urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('google_login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),

]
