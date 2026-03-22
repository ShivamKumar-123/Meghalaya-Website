from django.contrib import admin
from . models import MeghalayaImages,MeghalyaVideos,RegionOfMeghalaya,TrevalAround,Festival,MeghalayaLocation, VehicleOwner, Vehicle, VehicleBooking

# Register your models here.
class MeghalayaImageAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)


class MeghalyaVideosAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)


class RegionOfMeghalayaAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","updated_at")

class FestivalOfMeghalayaAdmin(admin.ModelAdmin):
    list_display = ("festival_name","created_at","updated_at")


class TrevalAroundAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)


class MeghalayaLocationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)



admin.site.register(TrevalAround, TrevalAroundAdmin)
admin.site.register(Festival,FestivalOfMeghalayaAdmin)
admin.site.register(RegionOfMeghalaya, RegionOfMeghalayaAdmin)
admin.site.register(MeghalayaImages, MeghalayaImageAdmin)
admin.site.register(MeghalyaVideos, MeghalyaVideosAdmin)
admin.site.register(MeghalayaLocation, MeghalayaLocationAdmin)


# ==================== VEHICLE BOOKING ADMIN ====================

class VehicleOwnerAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'owner_name', 'phone', 'city', 'is_verified', 'is_active', 'created_at')
    list_filter = ('is_verified', 'is_active', 'city')
    search_fields = ('business_name', 'owner_name', 'phone', 'email')
    list_editable = ('is_verified', 'is_active')
    ordering = ['-created_at']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_name', 'category', 'vehicle_number', 'owner', 'price_per_km', 'is_available', 'is_verified')
    list_filter = ('category', 'fuel_type', 'is_available', 'is_verified', 'ac_available')
    search_fields = ('vehicle_name', 'vehicle_number', 'owner__business_name')
    list_editable = ('is_available', 'is_verified')
    ordering = ['-created_at']


class VehicleBookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'passenger_name', 'vehicle', 'pickup_location', 'destination', 'pickup_date', 'booking_status', 'payment_status')
    list_filter = ('booking_status', 'payment_status', 'pickup_date')
    search_fields = ('booking_id', 'passenger_name', 'passenger_phone', 'pickup_location', 'destination')
    list_editable = ('booking_status', 'payment_status')
    readonly_fields = ('booking_id', 'created_at', 'updated_at')
    ordering = ['-created_at']
    
    fieldsets = (
        ('Booking Info', {
            'fields': ('booking_id', 'user', 'vehicle')
        }),
        ('Route Details', {
            'fields': ('pickup_location', 'destination', 'pickup_date', 'pickup_time', 'return_trip', 'return_date')
        }),
        ('Passenger Details', {
            'fields': ('passenger_name', 'passenger_phone', 'passenger_email', 'number_of_passengers', 'special_requests')
        }),
        ('Payment', {
            'fields': ('total_amount', 'payment_status', 'payment_screenshot', 'payment_date')
        }),
        ('Status', {
            'fields': ('booking_status', 'owner_remarks')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(VehicleOwner, VehicleOwnerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleBooking, VehicleBookingAdmin)