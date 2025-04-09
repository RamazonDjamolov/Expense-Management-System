from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils import timezone

from django.utils.deprecation import MiddlewareMixin


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)

        if user and user.is_authenticated:
            last_login = request.user.last_login
            if last_login:
                current_time = timezone.now()
                seconds_pas = (current_time - last_login).total_seconds()
                if seconds_pas > 10:
                    logout(request)
                    request.session.flush()

                    return redirect('account:login')

        response = self.get_response(request)
        return response

