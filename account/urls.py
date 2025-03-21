from django.shortcuts import render
from django.urls import path
from .views import google_login, google_callback

app_name = 'account'

urlpatterns = [
    path('google_login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),

]
