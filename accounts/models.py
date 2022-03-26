from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	lastname = models.CharField(max_length=30, null=True, blank=True)