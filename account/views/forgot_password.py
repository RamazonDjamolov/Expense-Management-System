from django.shortcuts import render
from django.views import View
from django.views.generic import FormView

from account.forms import ForgotPasswordForm
from account.models import User
from account.service import send_otp_code_email


class ForgotPasswordView(View):
    def get(self, request):
        form = ForgotPasswordForm()
        return render(request, 'accounts/forgot_password.html', context={'form': form})

    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            print(form,"my email")
            email = form.cleaned_data['email']
            print(email)
            # print(e,"my email")
            user = User.objects.filter(email=email).first()
            send_otp_code_email(email)
            return render(request, 'accounts/reset_password.html', context={'form': form})
        return render(request, 'accounts/forgot_password.html', context={'form': form})
