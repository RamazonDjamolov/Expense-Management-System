import email

from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data['password']
            re_password = cleaned_data['re_password']
            if password != re_password:
                raise ValidationError("password not equeal re_password")
            cleaned_data.pop('re_password')
            return cleaned_data

    # def save(self, commit=True):
    #     # user = User.objects.create_user(**self.cleaned_data)
    #     return user


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
