from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views import View

from account.forms import ForgotPasswordForm, RestorePasswordForm
from account.models import User
from account.service import send_email_async


class ForgotPasswordView(View):
    def get(self, request):
        form = ForgotPasswordForm()
        return render(request, template_name='accounts/forgot_password.html', context={'form': form})

    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['email']
            user = User.objects.filter(email=to).first()
            send_email_async(to, user)
            return HttpResponse('borib emailinga qara ')
        return render(request, template_name='accounts/forgot_password.html', context={'form': form})


class ResetPasswordView(View):
    def get(self, request):
        form = RestorePasswordForm()
        return render(request, template_name='accounts/restore_password.html', context={'form': form})

    def post(self, request):
        form = RestorePasswordForm(request.POST)
        if form.is_valid():
            form.update()
            return redirect('money:income_list')
        return render(request, template_name='accounts/restore_password.html', context={'form': form})
