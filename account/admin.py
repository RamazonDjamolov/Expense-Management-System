
from django.contrib import admin
from django.contrib.auth.models import Permission, Group

from account.models import User

# Register your models here
admin.site.register(User)


admin.site.register(Permission)




