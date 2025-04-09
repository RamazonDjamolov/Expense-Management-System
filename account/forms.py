import email
from django.utils import timezone

from django import forms
from django.core.exceptions import ValidationError

from account.models import User, Code, Profile


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
                raise ValidationError("password not equal  re_password")
            cleaned_data.pop('re_password')
            return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control     '}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        e = self.cleaned_data.get('email')
        if not User.objects.filter(email=e).exists():
            raise ValidationError("Email not Found")
        return cleaned_data


class RestorePasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        code = self.cleaned_data.get('code')
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        user = User.objects.filter(email=email).first()
        if not user:
            raise ValidationError("Email not Found")

        if not Code.objects.filter(code=code, user=user, expired_data__gt=timezone.now()):
            raise ValidationError(f"Code not Found {timezone.now()}")

        if password != re_password:
            raise ValidationError("password not equal  re_password")

        return self.cleaned_data

    def update(self):
        user = User.objects.filter(email=self.cleaned_data.get('email')).first()
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone_number']
