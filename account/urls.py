from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import path

from account.views import RegisterView, LogoutView, LoginView, GoogleRegisterView, GoogleCallbackView, AdminView, \
    ProfileDetailView, EditProfileView
from account.views.forgot_password import ForgotPasswordView, ResetPasswordView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('Logout/', LogoutView.as_view(), name='logout'),

    # google
    path('google_register/', GoogleRegisterView.as_view(), name='google_register'),
    path('google/callback/', GoogleCallbackView.as_view(), name='google_callback'),

    #     forgot password
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('restore_password/', ResetPasswordView.as_view(), name='restore_password'),

    #     for admin

    path('admin/', AdminView.as_view(), name='admin'),

    #     profile

    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:profile_id>/', EditProfileView.as_view(), name='profile_edit'),

]
