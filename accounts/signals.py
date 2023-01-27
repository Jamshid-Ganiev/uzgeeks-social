from django.db.models.signals import post_save
from django.dispatch import receiver

from models import CustomUser
from tasks import send_email


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_email.delay(
            "Welcome to Uzgeeks Social!",
            f"Hi, {instance.username}. Welcome to Uzgeeks Social. Enjoy the platform and posts.",
            [instance.email]
        )