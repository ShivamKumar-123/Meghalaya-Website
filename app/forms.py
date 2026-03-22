from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import VehicleOwner, Vehicle, VehicleBooking, AccommodationOwner, Accommodation, AccommodationBooking


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'Enter username'
            elif field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Enter password'
            elif field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm password'


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'username':
                field.widget.attrs['placeholder'] = 'Enter username'
            elif field_name == 'password':
                field.widget.attrs['placeholder'] = 'Enter password'


# ==================== VEHICLE BOOKING FORMS ====================
class VehicleOwnerRegistrationForm(forms.ModelForm):
    """Form for vehicle owner registration"""
    class Meta:
        model = VehicleOwner
        fields = ['business_name', 'owner_name', 'phone', 'alternate_phone', 'email', 
                  'address', 'city', 'profile_photo', 'id_proof', 'upi_id', 'qr_code']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Business/Service Name'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'alternate_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternate Phone (Optional)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Full Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'id_proof': forms.FileInput(attrs={'class': 'form-control'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UPI ID (e.g., name@upi)'}),
            'qr_code': forms.FileInput(attrs={'class': 'form-control'}),
        }


class VehicleForm(forms.ModelForm):
    """Form for adding/editing vehicles"""
    class Meta:
        model = Vehicle
        fields = ['category', 'vehicle_name', 'vehicle_number', 'vehicle_model', 'fuel_type',
                  'seating_capacity', 'ac_available', 'price_per_km', 'base_fare',
                  'vehicle_photo_1', 'vehicle_photo_2', 'vehicle_photo_3',
                  'registration_certificate', 'insurance_document', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'vehicle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Maruti Swift, Honda Activa'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., ML-01-AB-1234'}),
            'vehicle_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model Year/Name'}),
            'fuel_type': forms.Select(attrs={'class': 'form-control'}),
            'seating_capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'ac_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price_per_km': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price per KM', 'step': '0.50'}),
            'base_fare': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Fare', 'step': '0.50'}),
            'vehicle_photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'vehicle_photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'vehicle_photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'registration_certificate': forms.FileInput(attrs={'class': 'form-control'}),
            'insurance_document': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Vehicle description, features, etc.'}),
        }


class VehicleBookingForm(forms.ModelForm):
    """Form for booking a vehicle"""
    class Meta:
        model = VehicleBooking
        fields = ['pickup_location', 'destination', 'pickup_date', 'pickup_time',
                  'return_trip', 'return_date', 'passenger_name', 'passenger_phone',
                  'passenger_email', 'number_of_passengers', 'special_requests']
        widgets = {
            'pickup_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pickup Location'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pickup_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'return_trip': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'return_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'passenger_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'passenger_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'passenger_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (Optional)'}),
            'number_of_passengers': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any special requests...'}),
        }


class PaymentUploadForm(forms.Form):
    """Form for uploading payment screenshot"""
    payment_screenshot = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    )


# ==================== ACCOMMODATION BOOKING FORMS ====================
class AccommodationOwnerRegistrationForm(forms.ModelForm):
    """Form for accommodation owner registration"""
    class Meta:
        model = AccommodationOwner
        fields = ['business_name', 'owner_name', 'phone', 'alternate_phone', 'email', 
                  'address', 'city', 'profile_photo', 'id_proof', 'upi_id', 'qr_code']
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hotel/Property Name'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Owner Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'alternate_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternate Phone (Optional)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Full Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'id_proof': forms.FileInput(attrs={'class': 'form-control'}),
            'upi_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UPI ID (e.g., name@upi)'}),
            'qr_code': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AccommodationForm(forms.ModelForm):
    """Form for adding/editing accommodations"""
    class Meta:
        model = Accommodation
        fields = ['accommodation_type', 'name', 'room_type', 'address', 'city', 'landmark',
                  'google_maps_link', 'total_rooms', 'available_rooms', 'max_guests_per_room',
                  'bed_count', 'bathroom_attached', 'wifi_available', 'ac_available',
                  'tv_available', 'parking_available', 'restaurant_available', 'room_service',
                  'laundry_service', 'hot_water', 'power_backup', 'cctv', 'price_per_night',
                  'extra_person_charge', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
                  'description', 'house_rules', 'cancellation_policy']
        widgets = {
            'accommodation_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Property Name'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Full Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'landmark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nearby Landmark'}),
            'google_maps_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Google Maps Link'}),
            'total_rooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'available_rooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'max_guests_per_room': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'bed_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'bathroom_attached': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wifi_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ac_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tv_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'parking_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'restaurant_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'room_service': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'laundry_service': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'hot_water': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'power_backup': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cctv': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price_per_night': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price per Night', 'step': '1'}),
            'extra_person_charge': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Extra Person Charge', 'step': '1'}),
            'photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_4': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_5': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Property description, features, etc.'}),
            'house_rules': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Check-in/out times, pet policy, etc.'}),
            'cancellation_policy': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Cancellation policy'}),
        }


class AccommodationBookingForm(forms.ModelForm):
    """Form for booking accommodation"""
    class Meta:
        model = AccommodationBooking
        fields = ['check_in_date', 'check_out_date', 'number_of_rooms', 'number_of_guests',
                  'guest_name', 'guest_phone', 'guest_email', 'guest_id_type', 
                  'guest_id_number', 'special_requests']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number_of_rooms': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'guest_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'guest_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'guest_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (Optional)'}),
            'guest_id_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Type (Aadhar, Passport, etc.)'}),
            'guest_id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Number'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any special requests...'}),
        }


class AccommodationPaymentForm(forms.Form):
    """Form for uploading accommodation payment screenshot"""
    payment_screenshot = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
    )