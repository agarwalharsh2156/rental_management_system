from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
import ssl
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import MaintenanceRequestForm
from .models import Notification, MaintenanceRequest

def test_email(request):
    # Create an SSL context that does not verify certificates
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Create the email message
    email = EmailMessage(
        'Test Email',
        'This is a test email from Django.',
        settings.EMAIL_HOST_USER,
        ['recipient-email@example.com']  # Replace with tenant email
    )

    # Send the email using Django's email backend with the custom SSL context
    connection = email.get_connection(fail_silently=False)
    connection.ssl_context = ssl_context
    email.send()

    return HttpResponse('Test email sent!')

def tenant_notifications(request):
    if request.user.is_authenticated:
        # Fetch notifications from the Notification model
        user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    else:
        user_notifications = []  # Return an empty list if the user is not authenticated
    return render(request, 'notifications/notifications.html', {'notifications': user_notifications})

def tenant_dashboard(request):
    return render(request, 'notifications/dashboard.html')

def notifications_view(request):
    notifications = Notification.objects.all()  # Remove the user filter for now
    print(notifications)  # ✅ Confirm notifications exist
    return render(request, 'notifications.html', {'notifications': notifications})

def create_maintenance_request(request):
    if request.method == 'POST':
        form = MaintenanceRequestForm(request.POST)
        if form.is_valid():
            maintenance_request = form.save(commit=False)
            maintenance_request.tenant = request.user
            maintenance_request.save()
            # Create a notification for the property owner
            Notification.objects.create(
                user=maintenance_request.property.owner,
                message=f'Maintenance request raised by {request.user.username}: {maintenance_request.description}'
            )
            return redirect('notifications:my_notifications')  # Redirect after submission
    else:
        form = MaintenanceRequestForm()
    
    return render(request, 'notifications/create_maintenance_request.html', {'form': form})

def approve_maintenance_request(request, request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=request_id)

    if request.user == maintenance_request.property.owner:
        maintenance_request.status = 'approved'
        maintenance_request.save()

        # Send notification to tenant
        Notification.objects.create(
            user=maintenance_request.tenant,
            message=f"Your maintenance request for {maintenance_request.property.name} has been approved."
        )
        messages.success(request, "Maintenance request approved.")
    return redirect('notifications:my_notifications')

def reject_maintenance_request(request, request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=request_id)

    if request.user == maintenance_request.property.owner:
        maintenance_request.status = 'rejected'
        maintenance_request.save()

        # Send notification to tenant
        Notification.objects.create(
            user=maintenance_request.tenant,
            message=f"Your maintenance request for {maintenance_request.property.name} has been rejected."
        )
        messages.error(request, "Maintenance request rejected.")
    return redirect('notifications:my_notifications')

def maintenance_requests(request):
    if True:  # Temporarily bypass landlord check
        maintenance_requests = MaintenanceRequest.objects.all()
        return render(request, 'notifications/maintenance_requests.html', {
            'maintenance_requests': maintenance_requests
        })
    else:
        return render(request, 'notifications/maintenance_requests.html', {
            'maintenance_requests': []
        })