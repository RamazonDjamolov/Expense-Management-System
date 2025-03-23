from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    google_id = models.CharField(blank=True, null=True, max_length=255)
    image = models.URLField(blank=True, null=True)
