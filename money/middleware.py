from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.template.defaultfilters import first
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from account.models import User
from money.models import Files


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


class FilesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, 'user', None)
        print(request.path, "my path")
        print()
        if request.path.endswith('/upload_file/') and user.is_authenticated:
            group = request.user.groups.first()
            file_numer = Files.objects.filter(user=user).count()
            print(file_numer)
            if str(group) == 'client' and file_numer >= 5:
                return HttpResponseForbidden(" limit 5 files for clients")
        response = self.get_response(request)
        return response
