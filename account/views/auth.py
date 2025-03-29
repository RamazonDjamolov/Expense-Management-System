from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from account.forms import LoginRegistrationForm, RegisterForm


def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:login')

    return render(request, 'accounts/sign_in.html', context={'form': form})


def login_view(request):
    form = LoginRegistrationForm()
    if request.method == 'POST':
        print("post boldi ")
        form = LoginRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = authenticate(
                user=form.cleaned_data.get('user'),
                password=form.cleaned_data.get('password'),
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('money:income_list')
            form.add_error('password', 'Parol yoki username noto\'g\'ri !')

    return render(request, 'accounts/login.html', context={'form': form})
