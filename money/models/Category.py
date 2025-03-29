from account.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100, )
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name