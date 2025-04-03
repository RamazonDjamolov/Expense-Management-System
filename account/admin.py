from django.contrib import admin
from django.contrib.auth.models import Permission

from account.models import User


# Register your models here.
@admin.register(User)
class Admin(admin.ModelAdmin):
    pass

@admin.register(Permission)
class Admin(admin.ModelAdmin):
    pass