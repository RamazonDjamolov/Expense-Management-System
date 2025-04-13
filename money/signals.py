from django.dispatch import receiver
from django.db.models.signals import post_save

from config import settings
from .models import Category
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Files


@receiver(post_save, sender=Files)
def send_upload_notification(sender, instance, created, **kwargs):
    if created:
        subject = "Upload New File"
        message = f"New file has been uploaded.     {instance.file}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.user.email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
