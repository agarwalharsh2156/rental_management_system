from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.conf import settings
from .models import PropertyUnit
from notifications.models import Notification

@receiver(post_save, sender=PropertyUnit)
def notify_tenant_on_property_update(sender, instance, created, **kwargs):
    if not created and instance.tenant:
        # Create an in-app notification
        Notification.objects.create(
            tenant=instance.tenant,
            message=f'The property "{instance.name}" has been updated.'
        )
        
        # Send an email notification
        subject = 'Property Update Notification'
        message = f'Dear {instance.tenant.name},\n\nThe property "{instance.name}" has been updated.\n\nPlease check the details in your dashboard.'
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [instance.tenant.email])
        email.send()
