from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User


class Files(models.Model):
    name = models.CharField(_('name'), max_length=255)
    file = models.FileField(upload_to='uploads_files/')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='user_files')

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")
        db_table = 'files'



