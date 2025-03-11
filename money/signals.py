from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import Category


@receiver(post_save, sender=Category)
def default_user_post_save(sender, instance, created, **kwargs):
    if created:
        print('my signals ')

