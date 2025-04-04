from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView

from account.forms import LoginForm, RegisterForm
from account.models import User

from django.views import View


# my sign in
# def signup(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#
#             return redirect('money:income_list')
#
#     return render(request, 'accounts/sign_in.html', context={'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/sign_in.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            print(form.cleaned_data['password'])
            print(user, "my user")
            user.save()

            login(request, user)
            return redirect('money:income_list')
        return render(request, 'accounts/sign_in.html', context={'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         print("post boldi ")
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = User.objects.filter(username=username).first()
#
#             if user and user.check_password(password):
#                 login(request, user)
#
#                 return redirect('money:income_list')
#             form.add_error(None, 'email or password is incorrect')
#
#         return render(request, 'accounts/login.html', context={'form': form})
#
#     form = LoginForm()
#     return render(request, 'accounts/login.html', context={'form': form})
#


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email).first()

        if user and user.check_password(password):
            login(request, user)
            return redirect('money:income_list')
        form.add_error(None, 'email or password is incorrect')
        return render(request, 'accounts/login.html', context={'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', context={'form': form})


#  logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:login')
