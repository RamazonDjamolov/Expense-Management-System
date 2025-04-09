
from django.contrib import admin
from django.contrib.auth.models import Permission, Group

from account.models import User, Profile

# Register your models here
admin.site.register(User)


admin.site.register(Permission)

admin.site.register(Profile)


