from django.urls import path

from . import views



urlpatterns = [

    # Main route handled by app

    # Add more app-specific routes here if needed

    path('register/',views.register,name="register"),

    path('', views.home, name="home"),

    path('about/', views.about, name="about"),

    path('contact/', views.contact, name="contact"),

    path('my-messages/', views.my_messages, name="my_messages"),

    path('my-messages/<int:pk>/', views.message_reply, name="message_reply"),

    path('place/<str:name>/',views.allPlaces,name="allPlace"),

    

    # path('login/',views.login,name="login"),

    # path('logout/',views.logout,name="logout")

    path('regionOfMeghalaya/<str:name>/',views.regionMeghalaya,name="regionOfMeghalay"),

    path('festivalOfMeghalaya/<str:festival_name>/',views.festivalMeghalaya,name="festivalsOfMeghalaya"),

    path('trevalAround/<str:name>/',views.trevalAroundMeghalaya,name="trevalAroundOfMeghalaya"),

    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),

    path('terms-of-service/', views.terms_of_service, name="terms_of_service"),

    path('support/', views.support, name="support"),

    

    # ==================== VEHICLE BOOKING URLs ====================

    path('vehicles/', views.vehicle_list, name='vehicle_list'),

    path('vehicles/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),

    path('vehicles/<int:pk>/book/', views.book_vehicle, name='book_vehicle'),

    path('booking/<str:booking_id>/payment/', views.booking_payment, name='booking_payment'),

    path('booking/<str:booking_id>/status/', views.booking_status, name='booking_status'),

    path('my-bookings/', views.my_bookings, name='my_bookings'),

    

    # Vehicle Owner URLs

    path('vehicle-owner/login/', views.owner_login, name='owner_login'),

    path('vehicle-owner/register/', views.vehicle_owner_register, name='vehicle_owner_register'),

    path('vehicle-owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),

    path('vehicle-owner/vehicles/', views.owner_vehicles, name='owner_vehicles'),

    path('vehicle-owner/bookings/', views.owner_bookings, name='owner_bookings'),

    path('vehicle-owner/profile/', views.owner_profile, name='owner_profile'),

    path('vehicle-owner/add-vehicle/', views.add_vehicle, name='add_vehicle'),

    path('vehicle-owner/edit-vehicle/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),

    path('vehicle-owner/delete-vehicle/<int:pk>/', views.delete_vehicle, name='delete_vehicle'),

    path('vehicle-owner/manage-booking/<str:booking_id>/', views.manage_booking, name='manage_booking'),

    

    # ==================== ACCOMMODATION BOOKING URLs ====================

    path('accommodations/', views.accommodation_list, name='accommodation_list'),

    path('accommodations/<int:pk>/', views.accommodation_detail, name='accommodation_detail'),

    path('accommodations/<int:pk>/book/', views.book_accommodation, name='book_accommodation'),

    path('accommodation-booking/<str:booking_id>/payment/', views.accommodation_payment, name='accommodation_payment'),

    path('accommodation-booking/<str:booking_id>/', views.accommodation_booking_detail, name='accommodation_booking_detail'),

    path('my-accommodation-bookings/', views.my_accommodation_bookings, name='my_accommodation_bookings'),

    

    # Accommodation Owner URLs

    path('accommodation-owner/login/', views.accommodation_owner_login, name='accommodation_owner_login'),

    path('accommodation-owner/register/', views.accommodation_owner_register, name='accommodation_owner_register'),

    path('accommodation-owner/dashboard/', views.accommodation_owner_dashboard, name='accommodation_owner_dashboard'),

    path('accommodation-owner/accommodations/', views.accommodation_owner_accommodations, name='accommodation_owner_accommodations'),

    path('accommodation-owner/bookings/', views.accommodation_owner_bookings, name='accommodation_owner_bookings'),

    path('accommodation-owner/profile/', views.accommodation_owner_profile, name='accommodation_owner_profile'),

    path('accommodation-owner/add/', views.add_accommodation, name='add_accommodation'),

    path('accommodation-owner/edit/<int:pk>/', views.edit_accommodation, name='edit_accommodation'),

    path('accommodation-owner/delete/<int:pk>/', views.delete_accommodation, name='delete_accommodation'),

    path('accommodation-owner/manage-booking/<str:booking_id>/', views.manage_accommodation_booking, name='manage_accommodation_booking'),

]

