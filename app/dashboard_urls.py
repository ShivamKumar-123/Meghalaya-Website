from django.urls import path
from . import dashboard_views

urlpatterns = [
    # Dashboard Home
    path('', dashboard_views.dashboard_home, name='dashboard_home'),
    
    # Places CRUD
    path('places/', dashboard_views.dashboard_places, name='dashboard_places'),
    path('places/add/', dashboard_views.dashboard_places_add, name='dashboard_places_add'),
    path('places/<int:pk>/edit/', dashboard_views.dashboard_places_edit, name='dashboard_places_edit'),
    path('places/<int:pk>/delete/', dashboard_views.dashboard_places_delete, name='dashboard_places_delete'),
    
    # Regions CRUD
    path('regions/', dashboard_views.dashboard_regions, name='dashboard_regions'),
    path('regions/add/', dashboard_views.dashboard_regions_add, name='dashboard_regions_add'),
    path('regions/<int:pk>/edit/', dashboard_views.dashboard_regions_edit, name='dashboard_regions_edit'),
    path('regions/<int:pk>/delete/', dashboard_views.dashboard_regions_delete, name='dashboard_regions_delete'),
    
    # Festivals CRUD
    path('festivals/', dashboard_views.dashboard_festivals, name='dashboard_festivals'),
    path('festivals/add/', dashboard_views.dashboard_festivals_add, name='dashboard_festivals_add'),
    path('festivals/<int:pk>/edit/', dashboard_views.dashboard_festivals_edit, name='dashboard_festivals_edit'),
    path('festivals/<int:pk>/delete/', dashboard_views.dashboard_festivals_delete, name='dashboard_festivals_delete'),
    
    # Images CRUD
    path('images/', dashboard_views.dashboard_images, name='dashboard_images'),
    path('images/add/', dashboard_views.dashboard_images_add, name='dashboard_images_add'),
    path('images/<int:pk>/edit/', dashboard_views.dashboard_images_edit, name='dashboard_images_edit'),
    path('images/<int:pk>/delete/', dashboard_views.dashboard_images_delete, name='dashboard_images_delete'),
    
    # Videos CRUD
    path('videos/', dashboard_views.dashboard_videos, name='dashboard_videos'),
    path('videos/add/', dashboard_views.dashboard_videos_add, name='dashboard_videos_add'),
    path('videos/<int:pk>/edit/', dashboard_views.dashboard_videos_edit, name='dashboard_videos_edit'),
    path('videos/<int:pk>/delete/', dashboard_views.dashboard_videos_delete, name='dashboard_videos_delete'),
    
    # Travel Around CRUD
    path('travel/', dashboard_views.dashboard_travel, name='dashboard_travel'),
    path('travel/add/', dashboard_views.dashboard_travel_add, name='dashboard_travel_add'),
    path('travel/<int:pk>/edit/', dashboard_views.dashboard_travel_edit, name='dashboard_travel_edit'),
    path('travel/<int:pk>/delete/', dashboard_views.dashboard_travel_delete, name='dashboard_travel_delete'),
    
    # Users
    path('users/', dashboard_views.dashboard_users, name='dashboard_users'),
    
    # Messages
    path('messages/', dashboard_views.dashboard_messages, name='dashboard_messages'),
    path('messages/<int:pk>/', dashboard_views.dashboard_message_detail, name='dashboard_message_detail'),
    path('messages/<int:pk>/status/', dashboard_views.dashboard_message_status, name='dashboard_message_status'),
    path('messages/<int:pk>/delete/', dashboard_views.dashboard_message_delete, name='dashboard_message_delete'),
    
    # Vehicle Booking Management
    path('vehicle-owners/', dashboard_views.dashboard_vehicle_owners, name='dashboard_vehicle_owners'),
    path('vehicle-owners/<int:pk>/verify/', dashboard_views.dashboard_vehicle_owner_verify, name='dashboard_vehicle_owner_verify'),
    path('vehicles/', dashboard_views.dashboard_vehicles, name='dashboard_vehicles'),
    path('vehicles/<int:pk>/verify/', dashboard_views.dashboard_vehicle_verify, name='dashboard_vehicle_verify'),
    path('bookings/', dashboard_views.dashboard_bookings, name='dashboard_bookings'),
    path('bookings/<str:booking_id>/', dashboard_views.dashboard_booking_detail, name='dashboard_booking_detail'),
    
    # Accommodation Management
    path('accommodation-owners/', dashboard_views.dashboard_accommodation_owners, name='dashboard_accommodation_owners'),
    path('accommodation-owners/<int:pk>/action/', dashboard_views.dashboard_accommodation_owner_action, name='dashboard_accommodation_owner_action'),
    path('accommodations/', dashboard_views.dashboard_accommodations, name='dashboard_accommodations'),
    path('accommodations/<int:pk>/verify/', dashboard_views.dashboard_accommodation_verify, name='dashboard_accommodation_verify'),
    path('accommodation-bookings/', dashboard_views.dashboard_accommodation_bookings, name='dashboard_accommodation_bookings'),
    path('accommodation-bookings/<str:booking_id>/', dashboard_views.dashboard_accommodation_booking_detail, name='dashboard_accommodation_booking_detail'),
]
