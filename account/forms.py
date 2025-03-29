import email

from django import forms

from account.models import User


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',  'first_name', 'last_name', 'password',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control mb-2'}),
        }
