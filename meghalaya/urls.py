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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Keep this only
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
