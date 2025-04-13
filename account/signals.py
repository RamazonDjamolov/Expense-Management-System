from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from account.models import User, Profile
from django.contrib.auth.models import Group


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


@receiver(post_save, sender=User)
def add_group_to_user(sender, instance, created, **kwargs):
    if created:

        group = Group.objects.get(name="client")
        instance.groups.add(group)

        # group = Group.objects.get(name='client')
        # x = User.objects.filter(user=instance.id)
        # x.update(group=group)
