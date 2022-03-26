from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
	lastname = models.CharField(max_length=30, null=True, blank=True)


class Profile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=50, verbose_name="Name", null=True, blank=True)
	email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)
	address = models.CharField(max_length=50, verbose_name="Address", null=True, blank=True)
	address2 = models.CharField(max_length=50, verbose_name="Address2", null=True, blank=True)
	country = models.CharField(max_length=50, verbose_name="Couuntry", null=True, blank=True)
	zipp = models.CharField(max_length=50, verbose_name="Zip", null=True, blank=True)
	phone = models.CharField(max_length=50, verbose_name="Phone", null=True, blank=True)

	def __str__(self):
		return f"{self.user}, {self.name}"


	class Meta:
		verbose_name = "Profile"
		verbose_name_plural = "Profiles"

