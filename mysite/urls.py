from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints for the 'orders' app
    path('api/', include('orders.urls')),

    # Authentication endpoints (for token-based authentication)
    path('api/auth/', include('rest_framework.urls')),  # For session authentication
    # path('api/auth/', include('dj_rest_auth.urls')),  # For token authentication (optional)
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)