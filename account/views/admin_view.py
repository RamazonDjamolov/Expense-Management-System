from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from account.models import User

class AdminView(View):
    @method_decorator(permission_required('account.admin_permission', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        user = User.objects.all()
        return render(request, template_name='accounts/admin.html', context={'user': user})
