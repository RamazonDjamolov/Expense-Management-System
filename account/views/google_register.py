from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import View

from account.models import User
from config import settings
import requests


class GoogleRegisterView(View):
    def get(self, request):
        auth_url = (
            f"{settings.GOOGLE_AUTH_URL}"
            f"?client_id={settings.GOOGLE_CLIENT_ID}"
            f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
            f"&response_type=code"
            f"&scope=openid email profile"
        )
        return redirect(auth_url)


class GoogleCallbackView(View):
    def get(self, request):
        code = request.GET.get("code")
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        token_response = requests.post(settings.GOOGLE_TOKEN_URL, data=token_data)
        token_json = token_response.json()
        access_token = token_json.get("access_token")
        user_info_response = requests.get(settings.GOOGLE_USER_INFO_URL,
                                          headers={"Authorization": f"Bearer {access_token}"})
        user_info = user_info_response.json()

        user, _ = User.objects.get_or_create(email=user_info.get("email"), username=user_info.get("email"))
        login(request, user)
        return redirect('money:income_list')
