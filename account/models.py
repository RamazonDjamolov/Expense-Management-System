from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import datetime, timedelta
from django.utils.translation import gettext_lazy as _

def time_default():
    return datetime.now() + timedelta(seconds=60)


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, help_text='Email address')
    username = models.CharField(blank=True, null=True, max_length=255, help_text='username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Code(models.Model):
    code = models.CharField(blank=True, null=True, max_length=255, help_text=_('code'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code_user', help_text=_('user'))
    expired_data = models.DateTimeField(default=time_default, help_text=_('expired data'))


#  profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' , help_text=_('user'))
    image = models.ImageField(upload_to='profile_images', null=True, blank=True , default='profile_images/default.jpg', help_text=_('image') )
    bio = models.CharField(blank=True, null=True, max_length=255 , help_text=_('bio'), )
    phone_number = models.CharField(blank=True, null=True, max_length=255, help_text=_('phone number'))

    class Meta:
        db_table = 'Profile'
