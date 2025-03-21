from django.contrib.sites import requests
from django.shortcuts import render, redirect

from config.settings import GOOGLE_CLIENT_ID, GOOGLE_REDIRECT_URI
import urllib.parse


# Create your views here.
def google_login(request):
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "access_type": "offline",
        "prompt": "consent"
    }

    auth_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(auth_url, "my auth urls ")
    return redirect(auth_url)


import requests
from django.shortcuts import redirect, render
from django.contrib.auth import login

from django.contrib.auth.models import User


def google_callback(request):
    return redirect("money:income_list")
