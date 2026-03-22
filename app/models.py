from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class MeghalayaImages(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class MeghalyaVideos(models.Model):
    name = models.CharField(max_length=150)
    video = models.FileField(upload_to='videos/',blank=True, null=True)  # this is the key addition
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    

class RegionOfMeghalaya(models.Model):
    name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Festival(models.Model):
    festival_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/")
    description = models.TextField(default='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.festival_name
    


class TrevalAround(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="img/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class MeghalayaLocation(models.Model):
    name = models.CharField(max_length=100)
    placeUrl = models.URLField(
                max_length=300,
                blank=True,
                null=True,
                default='https://example.com',
                verbose_name='Place Website',
                help_text='Enter the official website of the place',
                unique=False
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('closed', 'Closed'),
    ]
    
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('booking', 'Booking Information'),
        ('feedback', 'Feedback'),
        ('partnership', 'Partnership'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_messages')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unread')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.status})"


class MessageReply(models.Model):
    message = models.ForeignKey(ContactMessage, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reply_text = models.TextField()
    is_admin_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Message Replies'
    
    def __str__(self):
        sender = "Admin" if self.is_admin_reply else self.user.username if self.user else "User"
        return f"Reply by {sender} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"


# ==================== VEHICLE BOOKING SYSTEM ====================

class VehicleOwner(models.Model):
    """Vehicle owner/provider profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vehicle_owner_profile')
    business_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100, default='Shillong')
    profile_photo = models.ImageField(upload_to='vehicle_owners/', blank=True, null=True)
    id_proof = models.ImageField(upload_to='vehicle_owners/id_proofs/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True, help_text='UPI ID for payments')
    qr_code = models.ImageField(upload_to='vehicle_owners/qr_codes/', blank=True, null=True, help_text='Payment QR Code')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.business_name} - {self.owner_name}"


class Vehicle(models.Model):
    """Vehicle details"""
    VEHICLE_CATEGORIES = [
        ('rickshaw', 'Auto Rickshaw'),
        ('taxi', 'Taxi'),
        ('car', 'Car'),
        ('bus', 'Bus'),
        ('bike', 'Bike'),
    ]
    
    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('cng', 'CNG'),
        ('electric', 'Electric'),
    ]
    
    owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, related_name='vehicles')
    category = models.CharField(max_length=20, choices=VEHICLE_CATEGORIES)
    vehicle_name = models.CharField(max_length=100, help_text='e.g., Maruti Swift, Honda Activa')
    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_model = models.CharField(max_length=100, blank=True, null=True)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES, default='petrol')
    seating_capacity = models.PositiveIntegerField(default=4)
    ac_available = models.BooleanField(default=False)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    base_fare = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Minimum fare')
    vehicle_photo_1 = models.ImageField(upload_to='vehicles/')
    vehicle_photo_2 = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    vehicle_photo_3 = models.ImageField(upload_to='vehicles/', blank=True, null=True)
    registration_certificate = models.ImageField(upload_to='vehicles/documents/', blank=True, null=True)
    insurance_document = models.ImageField(upload_to='vehicles/documents/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.vehicle_name} ({self.vehicle_number})"


class VehicleBooking(models.Model):
    """Booking details"""
    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    PAYMENT_STATUS = [
        ('pending', 'Payment Pending'),
        ('submitted', 'Payment Submitted'),
        ('verified', 'Payment Verified'),
        ('failed', 'Payment Failed'),
    ]
    
    booking_id = models.CharField(max_length=20, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle_bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='bookings')
    
    # Route details
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    return_trip = models.BooleanField(default=False)
    return_date = models.DateField(blank=True, null=True)
    
    # Passenger details
    passenger_name = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=15)
    passenger_email = models.EmailField(blank=True, null=True)
    number_of_passengers = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    
    # Pricing
    estimated_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_screenshot = models.ImageField(upload_to='payments/', blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    
    # Booking status
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    owner_remarks = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.booking_id:
            import random
            import string
            self.booking_id = 'BK' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.booking_id} - {self.passenger_name} ({self.booking_status})"


# ==================== ACCOMMODATION BOOKING SYSTEM ====================

class AccommodationOwner(models.Model):
    """Accommodation owner/provider profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accommodation_owner_profile')
    business_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100, default='Shillong')
    profile_photo = models.ImageField(upload_to='accommodation_owners/', blank=True, null=True)
    id_proof = models.ImageField(upload_to='accommodation_owners/id_proofs/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True, help_text='UPI ID for payments')
    qr_code = models.ImageField(upload_to='accommodation_owners/qr_codes/', blank=True, null=True, help_text='Payment QR Code')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.business_name} - {self.owner_name}"


class Accommodation(models.Model):
    """Accommodation details - Hotels, Hostels, Guest Houses, etc."""
    ACCOMMODATION_TYPES = [
        ('hotel', 'Hotel'),
        ('hostel', 'Hostel'),
        ('guest_house', 'Guest House'),
        ('homestay', 'Homestay'),
        ('resort', 'Resort'),
        ('lodge', 'Lodge'),
        ('cottage', 'Cottage'),
        ('apartment', 'Apartment'),
    ]
    
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('twin', 'Twin Room'),
        ('triple', 'Triple Room'),
        ('quad', 'Quad Room'),
        ('dormitory', 'Dormitory'),
        ('suite', 'Suite'),
        ('deluxe', 'Deluxe Room'),
        ('family', 'Family Room'),
    ]
    
    owner = models.ForeignKey(AccommodationOwner, on_delete=models.CASCADE, related_name='accommodations')
    accommodation_type = models.CharField(max_length=20, choices=ACCOMMODATION_TYPES)
    name = models.CharField(max_length=200, help_text='Name of the property')
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='double')
    
    # Location
    address = models.TextField()
    city = models.CharField(max_length=100, default='Shillong')
    landmark = models.CharField(max_length=200, blank=True, null=True)
    google_maps_link = models.URLField(blank=True, null=True)
    
    # Room details
    total_rooms = models.PositiveIntegerField(default=1)
    available_rooms = models.PositiveIntegerField(default=1)
    max_guests_per_room = models.PositiveIntegerField(default=2)
    bed_count = models.PositiveIntegerField(default=1)
    bathroom_attached = models.BooleanField(default=True)
    
    # Amenities
    wifi_available = models.BooleanField(default=False)
    ac_available = models.BooleanField(default=False)
    tv_available = models.BooleanField(default=False)
    parking_available = models.BooleanField(default=False)
    restaurant_available = models.BooleanField(default=False)
    room_service = models.BooleanField(default=False)
    laundry_service = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=True)
    power_backup = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    
    # Pricing
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    extra_person_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Photos
    photo_1 = models.ImageField(upload_to='accommodations/')
    photo_2 = models.ImageField(upload_to='accommodations/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='accommodations/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='accommodations/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='accommodations/', blank=True, null=True)
    
    # Description
    description = models.TextField(blank=True, null=True)
    house_rules = models.TextField(blank=True, null=True, help_text='Check-in/out times, pet policy, etc.')
    cancellation_policy = models.TextField(blank=True, null=True)
    
    # Status
    is_available = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    # Ratings
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    total_reviews = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_accommodation_type_display()}) - {self.city}"


class AccommodationBooking(models.Model):
    """Accommodation booking details"""
    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]
    
    PAYMENT_STATUS = [
        ('pending', 'Payment Pending'),
        ('submitted', 'Payment Submitted'),
        ('verified', 'Payment Verified'),
        ('failed', 'Payment Failed'),
        ('refunded', 'Refunded'),
    ]
    
    booking_id = models.CharField(max_length=20, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accommodation_bookings')
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='bookings')
    
    # Stay details
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_rooms = models.PositiveIntegerField(default=1)
    number_of_guests = models.PositiveIntegerField(default=1)
    
    # Guest details
    guest_name = models.CharField(max_length=100)
    guest_phone = models.CharField(max_length=15)
    guest_email = models.EmailField(blank=True, null=True)
    guest_id_type = models.CharField(max_length=50, blank=True, null=True, help_text='Aadhar, Passport, etc.')
    guest_id_number = models.CharField(max_length=50, blank=True, null=True)
    special_requests = models.TextField(blank=True, null=True)
    
    # Pricing
    number_of_nights = models.PositiveIntegerField(default=1)
    room_charges = models.DecimalField(max_digits=10, decimal_places=2)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Payment
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_screenshot = models.ImageField(upload_to='accommodation_payments/', blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    
    # Booking status
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    owner_remarks = models.TextField(blank=True, null=True)
    
    # Check-in/out times
    actual_check_in = models.DateTimeField(blank=True, null=True)
    actual_check_out = models.DateTimeField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.booking_id:
            import random
            import string
            self.booking_id = 'AC' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Calculate number of nights
        if self.check_in_date and self.check_out_date:
            self.number_of_nights = (self.check_out_date - self.check_in_date).days
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.booking_id} - {self.guest_name} ({self.booking_status})"


class AccommodationReview(models.Model):
    """Reviews for accommodations"""
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accommodation_reviews')
    booking = models.OneToOneField(AccommodationBooking, on_delete=models.CASCADE, related_name='review', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, help_text='Rating from 1 to 5')
    review_text = models.TextField()
    cleanliness_rating = models.PositiveIntegerField(default=5)
    location_rating = models.PositiveIntegerField(default=5)
    value_rating = models.PositiveIntegerField(default=5)
    service_rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Review by {self.user.username} for {self.accommodation.name}"