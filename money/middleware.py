from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from account.models import User


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)

        if user and user.is_authenticated:
            last_active = user.last_active
            current_time = now()

            if last_active:
                seconds_passed = (current_time - last_active).total_seconds()
                if seconds_passed > 604800:  # 7 kun kirmasa
                    logout(request)
                    request.session.flush()


            User.objects.filter(id=user.id).update(last_active=current_time)

        response = self.get_response(request)
        return response
