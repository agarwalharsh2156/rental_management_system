from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from RealEstate.models import Property_Unit

@receiver(post_save, sender=Property_Unit)
def notify_tenant(sender, instance, **kwargs):
    if kwargs.get('created', False) is False:
        subject = f"Update on Property Unit: {instance.name}"
        message = f"The property unit '{instance.name}' has been updated. New details:\n\n" \
                  f"Rooms: {instance.number_of_rooms}\nBathrooms: {instance.number_of_bathrooms}\n" \
                  f"Rent: {instance.rent} INR\nAvailability: {instance.availablity}\n\n" \
                  f"Please contact your landlord for further details."
        from_email = instance.property.owner_email
        to_email = [instance.property.lease_agreement.tenant_email]

        send_mail(subject, message, from_email, to_email)
