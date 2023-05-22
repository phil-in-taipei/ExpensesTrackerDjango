from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class UserProfile(models.Model):
    age = models.SmallIntegerField(null=True, blank=True)
    given_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=120, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserProfile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
