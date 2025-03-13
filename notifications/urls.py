from django.urls import path
from .views import test_email, tenant_notifications, tenant_dashboard, create_maintenance_request,approve_maintenance_request, reject_maintenance_request, maintenance_requests

urlpatterns = [
    path('test-email/', test_email, name='test_email'),
    path('my-notifications/', tenant_notifications, name='tenant_notifications'),
    path('dashboard/', tenant_dashboard, name='tenant_dashboard'),
    path('maintenance/create/', create_maintenance_request, name='create_maintenance_request'),
    path('approve-maintenance/<int:request_id>/', approve_maintenance_request, name='approve_maintenance'),
    path('reject-maintenance/<int:request_id>/', reject_maintenance_request, name='reject_maintenance'),
     path('maintenance-requests/', maintenance_requests, name='maintenance_requests'),
]
