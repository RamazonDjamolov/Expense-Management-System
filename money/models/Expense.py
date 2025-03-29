from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=100)
    category = models.ForeignKey('money.Category', on_delete=models.CASCADE)
    description = models.TextField(_('description'))
    created_at = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount) + ": category - > " + str(self.category)
