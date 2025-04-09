from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    amount = models.DecimalField(_('amount'), decimal_places=2, max_digits=100, help_text=_("amount"))
    category = models.ForeignKey('money.Category', on_delete=models.CASCADE, help_text=_("category"), )
    description = models.TextField(_('description'), help_text=_("description"), )
    created_at = models.DateField(_('created_at'), auto_now_add=True, help_text=_("created at"))
    is_deleted = models.BooleanField(_('is deleted'), default=False, help_text=_("is deleted"))
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, help_text=_('user'))

    def __str__(self):
        return str(self.amount) + ": category - > " + str(self.category)

    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")
