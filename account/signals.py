from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from account.models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if not created:
        profile = Profile.objects.filter(user=instance).exists()
        if profile:
            pass
        else:
            Profile.objects.create(user=instance)
            print("created not")
    #         ozgartirilvotganda
    else:
        Profile.objects.create(user=instance)
        print("created")
#         yangi yaratilingan payti
