# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

# # Serve static files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# # Serve media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Keep this only
    # Custom login view with styled form
    path('accounts/login/', auth_views.LoginView.as_view(
        authentication_form=CustomAuthenticationForm
    ), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # For other auth URLs
    path('accounts/', include('allauth.urls')),  # Allauth URLs for social login
    path('dashboard/', include('app.dashboard_urls')),  # Admin Dashboard
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
