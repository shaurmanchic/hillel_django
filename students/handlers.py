from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def phone_edit_handler(sender, **kwargs):
    if phone := kwargs['instance'].phone:
        kwargs['instance'].phone = int(phone.strip('').replace('+', '').replace('(', '').replace(')', ''))
