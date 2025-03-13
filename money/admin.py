from django.contrib import admin
from django.contrib.auth.models import User

from money.models import Category, Income, Expense

# Register your models here.
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Expense)
