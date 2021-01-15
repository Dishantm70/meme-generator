from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from common.models import Common


class User(AbstractUser, Common):
    cookie_consent_accepted = models.BooleanField(default=False)