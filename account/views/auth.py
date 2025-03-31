from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm
from account.models import User


# my sign in
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return redirect('money:income_list')

    return render(request, 'accounts/sign_in.html', context={'form': form})


#  my login view


def login_view(request):
    if request.method == 'POST':
        print("post boldi ")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                login(request, user)

                return redirect('money:income_list')
            form.add_error(None, 'Username or password is incorrect')

            return render(request, 'accounts/login.html', context={'form': form})

    form = LoginForm()
    return render(request, 'accounts/login.html', context={'form': form})


#  logout
def logout_view(request):
    logout(request)
    return redirect('account:login')
