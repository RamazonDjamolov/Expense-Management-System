from django.contrib.auth import login
from django.contrib.sites import requests
from django.shortcuts import redirect

from account.models import User
from config.settings import GOOGLE_CLIENT_ID, GOOGLE_REDIRECT_URI, GOOGLE_AUTH_URL, GOOGLE_CLIENT_SECRET, \
    GOOGLE_TOKEN_URL, GOOGLE_USER_INFO_URL
import requests




# Create your views here.
def google_login(request):
    auth_url = (
        f"{GOOGLE_AUTH_URL}"
        f"?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
        f"&response_type=code"
        f"&scope=openid email profile"
    )
    return redirect(auth_url)


def google_callback(request):
    code = request.GET.get("code")
    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",

    }
    token_response = requests.post(GOOGLE_TOKEN_URL, data=token_data)
    token_data = token_response.json()
    access_token = token_data.get("access_token")

    user_info_response = requests.get(GOOGLE_USER_INFO_URL,
                                      headers={"Authorization": f"Bearer {access_token}"})

    user_info = user_info_response.json()
    # print(user_info_response.json(), "my user info ")

    user, _ = User.objects.get_or_create(google_id=user_info.get('id'),
                                         email=user_info.get('email'),
                                         image=user_info.get('picture'),
                                         username=user_info.get('email'),
                                         )
    # print(user, "mys user info ")
    # print(_, "mys user info2 ")
    login(request, user)
    return redirect("money:income_list")

    # return HttpResponse('google login success')
