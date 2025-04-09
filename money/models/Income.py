from account.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Income(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=100, help_text=_("amount"))
    category = models.ForeignKey('money.Category', on_delete=models.CASCADE, help_text=_("category"))
    description = models.TextField(_('description'), help_text=_("description"))
    created_at = models.DateField(auto_now_add=True, help_text=_("created at"))
    is_deleted = models.BooleanField(default=False, help_text=_("is deleted"))
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, help_text=_('user'))

    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")
        db_table = 'income'

    def __str__(self):
        return str(self.amount)
