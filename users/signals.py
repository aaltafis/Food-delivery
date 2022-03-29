from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import CustomUser, Profile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """ При регистрации пользователя профиль создается автоматически """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """ Вызывается метод save из модели Profile """
    instance.profile.save()
