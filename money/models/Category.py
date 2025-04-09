from account.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(_('name'), max_length=100, help_text=_("name"))
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, help_text=_('user'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'category'

    def __str__(self):
        return self.name