from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm
from account.models import User

from django.views import View


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, template_name='accounts/sign_in.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)
            return redirect('money:income_list')
        return render(request, template_name='accounts/sign_in.html', context={'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, template_name='accounts/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)
                return redirect('money:income_list')
            form.add_error(None, 'password or username incorrect')
        return render(request, template_name='accounts/login.html', context={'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:login')
