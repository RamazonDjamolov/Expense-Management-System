from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import datetime, timedelta


def time_default():
    return datetime.now() + timedelta(seconds=60)


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, null=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Code(models.Model):
    code = models.CharField(blank=True, null=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='code_user')
    expired_data = models.DateTimeField(default=time_default)


#  profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images', null=True, blank=True , default='profile_images/default.jpg')
    bio = models.CharField(blank=True, null=True, max_length=255)
    phone_number = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'Profile'
