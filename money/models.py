from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100, )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(_('description'))
    created_at = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



    class Meta:
        db_table = 'income'

    def __str__(self):
        return str(self.amount)

class Expense(models.Model):
    amount = models.DecimalField( decimal_places=2, max_digits=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(_('description'))
    created_at = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.amount) + ": category - > " + str(self.category)