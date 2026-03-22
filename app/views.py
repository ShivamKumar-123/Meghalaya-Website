from django.shortcuts import render, redirect, get_object_or_404

from . models import MeghalayaImages,MeghalyaVideos,RegionOfMeghalaya, Festival, TrevalAround,MeghalayaLocation, ContactMessage, MessageReply, AccommodationOwner, Accommodation, AccommodationBooking

from .forms import UserRegistrationForm, AccommodationOwnerRegistrationForm, AccommodationForm, AccommodationBookingForm, AccommodationPaymentForm

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.mail import send_mail

from django.conf import settings

from django.utils import timezone

from decimal import Decimal



# Create your views here.





# @login_required

# def home(request):

#     meghaData = MeghalayaImages.objects.all()

#     return render(request,"website/home.html",{"meghaData":meghaData})




def home(request):

    meghaData = MeghalayaImages.objects.all()

    # placeName = MeghalayaImages.objects.values_list('name', flat=True).distinct()

    placeName = MeghalayaImages.objects.values('name').exclude(

    name__in=["Cherrapunji", "Police Bazar", "Seven Sister Falls", "Dawki River", "Cathedral of Mary"]

    ).distinct()



    regionName= RegionOfMeghalaya.objects.values('name').distinct()

    festivalnames = Festival.objects.values('festival_name').distinct()

    trevalPlace = TrevalAround.objects.values('name').distinct()







    return render(request,"website/home.html",{"meghaData":meghaData,"placeName":placeName,"regionName":regionName,"festivalnames":festivalnames,"trevalPlace":trevalPlace})





def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password1'])

            user.save()

            login(request, user)

            return redirect('home')





    else:

        form = UserRegistrationForm()





    return render(request,'registration/register.html',{'form':form})





# def allPlaces(request):

#     mydata = MeghalayaImages.objects.all()

#     return render(request, 'allPlaces.html', {"mydata": mydata})



def allPlaces(request, name):

    mydata = MeghalayaImages.objects.filter(name=name)

    mydataVideo = MeghalyaVideos.objects.filter(name=name)

    location = MeghalayaLocation.objects.filter(name=name).first()

    print(location)

    return render(request, 'allPlaces.html', {

        "mydata": mydata,

        "mydataVideo": mydataVideo,

        "location": location

    })





def regionMeghalaya(request, name):

    mydata = RegionOfMeghalaya.objects.filter(name=name)

    mydataVideo = MeghalyaVideos.objects.filter(name=name)

    return render(request,"regionMegha.html",{"mydata": mydata,"mydataVideo": mydataVideo,})



def festivalMeghalaya(request,festival_name):

    mydata = Festival.objects.filter(festival_name=festival_name)

    return render(request,"festival.html",{"mydata":mydata})



def trevalAroundMeghalaya(request,name):

    mydata = TrevalAround.objects.filter(name=name)

    return render(request,"trevalAround.html",{"mydata":mydata})





def about(request):

    return render(request, 'website/about.html')





def contact(request):

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        phone = request.POST.get('phone', '')

        subject = request.POST.get('subject')

        message_text = request.POST.get('message')

        

        # Save message to database

        contact_msg = ContactMessage.objects.create(

            user=request.user if request.user.is_authenticated else None,

            name=name,

            email=email,

            phone=phone,

            subject=subject,

            message=message_text

        )

        

        # Send email notification (optional)

        try:

            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\n\nMessage:\n{message_text}"

            send_mail(

                f'Contact Form: {subject}',

                full_message,

                email,

                [settings.EMAIL_HOST_USER],

                fail_silently=True,

            )

        except:

            pass

        

        messages.success(request, 'Thank you for your message! We will get back to you soon.')

        return redirect('contact')

    

    return render(request, 'website/contact.html')





@login_required

def my_messages(request):

    """View for users to see their messages and replies"""

    user_messages = ContactMessage.objects.filter(

        email=request.user.email

    ) | ContactMessage.objects.filter(user=request.user)

    

    return render(request, 'website/my_messages.html', {'user_messages': user_messages})





@login_required

def message_reply(request, pk):

    """Allow users to reply to their messages"""

    contact_msg = get_object_or_404(ContactMessage, pk=pk)

    

    # Check if user owns this message

    if contact_msg.user != request.user and contact_msg.email != request.user.email:

        messages.error(request, 'You do not have permission to view this message.')

        return redirect('my_messages')

    

    if request.method == 'POST':

        reply_text = request.POST.get('reply_text')

        if reply_text:

            MessageReply.objects.create(

                message=contact_msg,

                user=request.user,

                reply_text=reply_text,

                is_admin_reply=False

            )

            messages.success(request, 'Your reply has been sent!')

            return redirect('message_reply', pk=pk)

    

    replies = contact_msg.replies.all()

    

    return render(request, 'website/message_detail.html', {

        'contact_message': contact_msg,

        'replies': replies,

    })





def privacy_policy(request):

    """Privacy Policy page"""

    return render(request, 'website/privacy_policy.html')





def terms_of_service(request):

    """Terms of Service page"""

    return render(request, 'website/terms_of_service.html')





def support(request):

    """Support page"""

    return render(request, 'website/support.html')





# ==================== VEHICLE BOOKING VIEWS ====================

from .models import VehicleOwner, Vehicle, VehicleBooking

from .forms import VehicleOwnerRegistrationForm, VehicleForm, VehicleBookingForm, PaymentUploadForm

from django.utils import timezone

from django.db.models import Q





def vehicle_list(request):

    """List all available vehicles with filtering"""

    category = request.GET.get('category', '')

    

    vehicles = Vehicle.objects.filter(is_available=True, is_verified=True, owner__is_verified=True, owner__is_active=True)

    

    if category:

        vehicles = vehicles.filter(category=category)

    

    categories = Vehicle.VEHICLE_CATEGORIES

    

    return render(request, 'vehicles/vehicle_list.html', {

        'vehicles': vehicles,

        'categories': categories,

        'selected_category': category,

    })





def vehicle_detail(request, pk):

    """View vehicle details with owner info"""

    vehicle = get_object_or_404(Vehicle, pk=pk, is_available=True)

    

    return render(request, 'vehicles/vehicle_detail.html', {

        'vehicle': vehicle,

    })





@login_required

def book_vehicle(request, pk):

    """Book a vehicle - fill booking form"""

    vehicle = get_object_or_404(Vehicle, pk=pk, is_available=True)

    

    if request.method == 'POST':

        form = VehicleBookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.vehicle = vehicle

            booking.total_amount = vehicle.base_fare  # Initial amount, can be calculated based on distance

            booking.save()

            messages.success(request, 'Booking created! Please proceed to payment.')

            return redirect('booking_payment', booking_id=booking.booking_id)

    else:

        initial_data = {

            'passenger_name': request.user.get_full_name() or request.user.username,

            'passenger_email': request.user.email,

        }

        form = VehicleBookingForm(initial=initial_data)

    

    return render(request, 'vehicles/book_vehicle.html', {

        'vehicle': vehicle,

        'form': form,

    })





@login_required

def booking_payment(request, booking_id):

    """Payment page with QR code"""

    booking = get_object_or_404(VehicleBooking, booking_id=booking_id, user=request.user)

    

    if booking.payment_status == 'verified':

        messages.info(request, 'Payment already verified for this booking.')

        return redirect('booking_status', booking_id=booking_id)

    

    if request.method == 'POST':

        form = PaymentUploadForm(request.POST, request.FILES)

        if form.is_valid():

            booking.payment_screenshot = form.cleaned_data['payment_screenshot']

            booking.payment_status = 'submitted'

            booking.payment_date = timezone.now()

            booking.save()

            messages.success(request, 'Payment screenshot uploaded! Waiting for verification.')

            return redirect('booking_status', booking_id=booking_id)

    else:

        form = PaymentUploadForm()

    

    return render(request, 'vehicles/booking_payment.html', {

        'booking': booking,

        'form': form,

    })





@login_required

def booking_status(request, booking_id):

    """View booking status"""

    booking = get_object_or_404(VehicleBooking, booking_id=booking_id, user=request.user)

    

    return render(request, 'vehicles/booking_status.html', {

        'booking': booking,

    })





@login_required

def my_bookings(request):

    """List user's bookings"""

    bookings = VehicleBooking.objects.filter(user=request.user)

    

    return render(request, 'vehicles/my_bookings.html', {

        'bookings': bookings,

    })





# ==================== VEHICLE OWNER VIEWS ====================



def owner_login(request):

    """Login page for vehicle owners"""

    from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

    

    # If already logged in as vehicle owner, go to dashboard

    if request.user.is_authenticated and hasattr(request.user, 'vehicle_owner_profile'):

        return redirect('owner_dashboard')

    

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        

        if user is not None:

            if hasattr(user, 'vehicle_owner_profile'):

                auth_login(request, user)

                messages.success(request, f'Welcome back, {user.vehicle_owner_profile.business_name}!')

                return redirect('owner_dashboard')

            else:

                messages.error(request, 'This account is not registered as a vehicle owner.')

        else:

            messages.error(request, 'Invalid username or password.')

    

    return render(request, 'vehicles/owner_login.html')





def vehicle_owner_register(request):

    """Register as a vehicle owner"""

    if request.user.is_authenticated and hasattr(request.user, 'vehicle_owner_profile'):

        messages.info(request, 'You are already registered as a vehicle owner.')

        return redirect('owner_dashboard')

    

    if request.method == 'POST':

        form = VehicleOwnerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            owner = form.save(commit=False)

            if request.user.is_authenticated:

                owner.user = request.user

            else:

                # Create a user account for the owner

                from django.contrib.auth.models import User

                username = form.cleaned_data['email'].split('@')[0]

                base_username = username

                counter = 1

                while User.objects.filter(username=username).exists():

                    username = f"{base_username}{counter}"

                    counter += 1

                user = User.objects.create_user(

                    username=username,

                    email=form.cleaned_data['email'],

                    password='changeme123'  # They should change this

                )

                owner.user = user

                login(request, user)

            owner.save()

            messages.success(request, 'Registration successful! Your account is pending verification.')

            return redirect('owner_dashboard')

    else:

        form = VehicleOwnerRegistrationForm()

    

    return render(request, 'vehicles/owner_register.html', {

        'form': form,

    })





@login_required

def owner_dashboard(request):

    """Vehicle owner dashboard"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not registered as a vehicle owner.')

        return redirect('vehicle_owner_register')

    

    vehicles = owner.vehicles.all()

    bookings = VehicleBooking.objects.filter(vehicle__owner=owner).order_by('-created_at')

    pending_bookings = bookings.filter(booking_status='pending', payment_status='submitted')

    confirmed_bookings = bookings.filter(booking_status='confirmed')

    in_progress_bookings = bookings.filter(booking_status='in_progress')

    completed_bookings = bookings.filter(booking_status='completed')

    

    return render(request, 'vehicles/owner_dashboard_new.html', {

        'owner': owner,

        'vehicles': vehicles,

        'bookings': bookings,

        'pending_bookings': pending_bookings,

        'pending_count': pending_bookings.count(),

        'confirmed_bookings': confirmed_bookings,

        'in_progress_bookings': in_progress_bookings,

        'completed_bookings': completed_bookings,

    })





@login_required

def add_vehicle(request):

    """Add a new vehicle"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You must be a registered vehicle owner to add vehicles.')

        return redirect('vehicle_owner_register')

    

    if request.method == 'POST':

        form = VehicleForm(request.POST, request.FILES)

        if form.is_valid():

            vehicle = form.save(commit=False)

            vehicle.owner = owner

            vehicle.save()

            messages.success(request, 'Vehicle added successfully! It will be visible after verification.')

            return redirect('owner_dashboard')

    else:

        form = VehicleForm()

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/add_vehicle_new.html', {

        'form': form,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def edit_vehicle(request, pk):

    """Edit a vehicle"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not authorized.')

        return redirect('home')

    

    vehicle = get_object_or_404(Vehicle, pk=pk, owner=owner)

    

    if request.method == 'POST':

        form = VehicleForm(request.POST, request.FILES, instance=vehicle)

        if form.is_valid():

            form.save()

            messages.success(request, 'Vehicle updated successfully!')

            return redirect('owner_dashboard')

    else:

        form = VehicleForm(instance=vehicle)

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/edit_vehicle_new.html', {

        'form': form,

        'vehicle': vehicle,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def delete_vehicle(request, pk):

    """Delete a vehicle"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not authorized.')

        return redirect('home')

    

    vehicle = get_object_or_404(Vehicle, pk=pk, owner=owner)

    

    if request.method == 'POST':

        vehicle.delete()

        messages.success(request, 'Vehicle deleted successfully!')

        return redirect('owner_dashboard')

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/delete_vehicle_new.html', {

        'vehicle': vehicle,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def manage_booking(request, booking_id):

    """Vehicle owner manages a booking (confirm/reject)"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not authorized.')

        return redirect('home')

    

    booking = get_object_or_404(VehicleBooking, booking_id=booking_id, vehicle__owner=owner)

    

    if request.method == 'POST':

        action = request.POST.get('action')

        remarks = request.POST.get('remarks', '')

        

        if action == 'confirm':

            booking.booking_status = 'confirmed'

            booking.payment_status = 'verified'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Booking confirmed!')

        elif action == 'reject':

            booking.booking_status = 'cancelled'

            booking.payment_status = 'failed'

            booking.owner_remarks = remarks

            booking.save()

            messages.warning(request, 'Booking rejected.')

        elif action == 'in_progress':

            booking.booking_status = 'in_progress'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Trip started! Status updated to In Progress.')

        elif action == 'complete':

            booking.booking_status = 'completed'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Booking marked as completed!')

        

        return redirect('owner_dashboard')

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/manage_booking_new.html', {

        'booking': booking,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def owner_vehicles(request):

    """Owner's vehicles list page"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not registered as a vehicle owner.')

        return redirect('vehicle_owner_register')

    

    vehicles = owner.vehicles.all()

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/owner_vehicles.html', {

        'owner': owner,

        'vehicles': vehicles,

        'pending_count': pending_count,

    })





@login_required

def owner_bookings(request):

    """Owner's bookings list page with filtering"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not registered as a vehicle owner.')

        return redirect('vehicle_owner_register')

    

    status_filter = request.GET.get('status', '')

    bookings = VehicleBooking.objects.filter(vehicle__owner=owner).order_by('-created_at')

    

    if status_filter == 'pending':

        bookings = bookings.filter(booking_status='pending', payment_status='submitted')

    elif status_filter == 'confirmed':

        bookings = bookings.filter(booking_status='confirmed')

    elif status_filter == 'in_progress':

        bookings = bookings.filter(booking_status='in_progress')

    elif status_filter == 'completed':

        bookings = bookings.filter(booking_status='completed')

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/owner_bookings.html', {

        'owner': owner,

        'bookings': bookings,

        'status_filter': status_filter,

        'pending_count': pending_count,

    })





@login_required

def owner_profile(request):

    """Owner profile settings page"""

    try:

        owner = request.user.vehicle_owner_profile

    except VehicleOwner.DoesNotExist:

        messages.error(request, 'You are not registered as a vehicle owner.')

        return redirect('vehicle_owner_register')

    

    if request.method == 'POST':

        owner.business_name = request.POST.get('business_name', owner.business_name)

        owner.phone = request.POST.get('phone', owner.phone)

        owner.alternate_phone = request.POST.get('alternate_phone', owner.alternate_phone)

        owner.address = request.POST.get('address', owner.address)

        owner.city = request.POST.get('city', owner.city)

        owner.upi_id = request.POST.get('upi_id', owner.upi_id)

        

        if 'profile_photo' in request.FILES:

            owner.profile_photo = request.FILES['profile_photo']

        if 'qr_code' in request.FILES:

            owner.qr_code = request.FILES['qr_code']

        

        owner.save()

        messages.success(request, 'Profile updated successfully!')

        return redirect('owner_profile')

    

    pending_count = VehicleBooking.objects.filter(

        vehicle__owner=owner, 

        booking_status='pending', 

        payment_status='submitted'

    ).count()

    

    return render(request, 'vehicles/owner_profile.html', {

        'owner': owner,

        'pending_count': pending_count,

    })





# ==================== ACCOMMODATION BOOKING SYSTEM ====================



def accommodation_list(request):

    """List all available accommodations"""

    accommodations = Accommodation.objects.filter(is_available=True, is_verified=True)

    

    # Filter by type

    acc_type = request.GET.get('type')

    if acc_type:

        accommodations = accommodations.filter(accommodation_type=acc_type)

    

    # Filter by city

    city = request.GET.get('city')

    if city:

        accommodations = accommodations.filter(city__icontains=city)

    

    # Filter by price range

    min_price = request.GET.get('min_price')

    max_price = request.GET.get('max_price')

    if min_price:

        accommodations = accommodations.filter(price_per_night__gte=min_price)

    if max_price:

        accommodations = accommodations.filter(price_per_night__lte=max_price)

    

    # Get unique cities for filter

    cities = Accommodation.objects.filter(is_available=True, is_verified=True).values_list('city', flat=True).distinct()

    

    return render(request, 'accommodations/accommodation_list.html', {

        'accommodations': accommodations,

        'cities': cities,

        'accommodation_types': Accommodation.ACCOMMODATION_TYPES,

        'selected_type': acc_type,

        'selected_city': city,

    })





def accommodation_detail(request, pk):

    """View accommodation details"""

    accommodation = get_object_or_404(Accommodation, pk=pk)

    similar_accommodations = Accommodation.objects.filter(

        accommodation_type=accommodation.accommodation_type,

        is_available=True,

        is_verified=True

    ).exclude(pk=pk)[:4]

    

    return render(request, 'accommodations/accommodation_detail.html', {

        'accommodation': accommodation,

        'similar_accommodations': similar_accommodations,

    })





@login_required

def book_accommodation(request, pk):

    """Book an accommodation"""

    accommodation = get_object_or_404(Accommodation, pk=pk)

    

    if request.method == 'POST':

        form = AccommodationBookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.accommodation = accommodation

            

            # Calculate pricing

            check_in = form.cleaned_data['check_in_date']

            check_out = form.cleaned_data['check_out_date']

            num_rooms = form.cleaned_data['number_of_rooms']

            num_guests = form.cleaned_data['number_of_guests']

            

            nights = (check_out - check_in).days

            room_charges = accommodation.price_per_night * nights * num_rooms

            

            # Extra person charges

            extra_guests = max(0, num_guests - (accommodation.max_guests_per_room * num_rooms))

            extra_charges = Decimal(extra_guests) * accommodation.extra_person_charge * nights

            

            booking.number_of_nights = nights

            booking.room_charges = room_charges

            booking.extra_charges = extra_charges

            booking.total_amount = room_charges + extra_charges

            

            booking.save()

            messages.success(request, 'Booking created! Please complete the payment.')

            return redirect('accommodation_payment', booking_id=booking.booking_id)

    else:

        initial_data = {

            'guest_name': request.user.get_full_name() or request.user.username,

            'guest_email': request.user.email,

        }

        form = AccommodationBookingForm(initial=initial_data)

    

    return render(request, 'accommodations/book_accommodation.html', {

        'accommodation': accommodation,

        'form': form,

    })





@login_required

def accommodation_payment(request, booking_id):

    """Handle accommodation payment"""

    booking = get_object_or_404(AccommodationBooking, booking_id=booking_id, user=request.user)

    

    if booking.payment_status == 'verified':

        messages.info(request, 'Payment already verified for this booking.')

        return redirect('accommodation_booking_detail', booking_id=booking.booking_id)

    

    if request.method == 'POST':

        form = AccommodationPaymentForm(request.POST, request.FILES)

        if form.is_valid():

            booking.payment_screenshot = form.cleaned_data['payment_screenshot']

            booking.payment_status = 'submitted'

            booking.payment_date = timezone.now()

            booking.save()

            messages.success(request, 'Payment submitted successfully! Waiting for verification.')

            return redirect('accommodation_booking_detail', booking_id=booking.booking_id)

    else:

        form = AccommodationPaymentForm()

    

    return render(request, 'accommodations/accommodation_payment.html', {

        'booking': booking,

        'form': form,

    })





@login_required

def accommodation_booking_detail(request, booking_id):

    """View booking details"""

    booking = get_object_or_404(AccommodationBooking, booking_id=booking_id, user=request.user)

    return render(request, 'accommodations/accommodation_booking_detail.html', {

        'booking': booking,

    })





@login_required

def my_accommodation_bookings(request):

    """List user's accommodation bookings"""

    bookings = AccommodationBooking.objects.filter(user=request.user)

    return render(request, 'accommodations/my_bookings.html', {

        'bookings': bookings,

    })





# ==================== ACCOMMODATION OWNER VIEWS ====================



@login_required

def accommodation_owner_register(request):

    """Register as accommodation owner"""

    # Check if user is already registered as owner

    try:

        owner = request.user.accommodation_owner_profile

        messages.info(request, 'You are already registered as an accommodation owner.')

        return redirect('accommodation_owner_dashboard')

    except AccommodationOwner.DoesNotExist:

        pass

    

    if request.method == 'POST':

        form = AccommodationOwnerRegistrationForm(request.POST, request.FILES)

        if form.is_valid():

            owner = form.save(commit=False)

            owner.user = request.user

            owner.save()

            messages.success(request, 'Registration successful! Your account is pending verification.')

            return redirect('accommodation_owner_dashboard')

    else:

        form = AccommodationOwnerRegistrationForm()

    

    return render(request, 'accommodations/owner_register.html', {

        'form': form,

    })





@login_required

def accommodation_owner_login(request):

    """Redirect to accommodation owner dashboard"""

    try:

        owner = request.user.accommodation_owner_profile

        return redirect('accommodation_owner_dashboard')

    except AccommodationOwner.DoesNotExist:

        messages.error(request, 'You are not registered as an accommodation owner.')

        return redirect('accommodation_owner_register')





@login_required

def accommodation_owner_dashboard(request):

    """Accommodation owner dashboard"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        messages.error(request, 'Please register as an accommodation owner first.')

        return redirect('accommodation_owner_register')

    

    accommodations = owner.accommodations.all()

    

    # Get bookings for owner's accommodations

    pending_bookings = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    )

    confirmed_bookings = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='confirmed'

    )

    checked_in_bookings = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='checked_in'

    )

    

    pending_count = pending_bookings.count()

    

    return render(request, 'accommodations/owner_dashboard.html', {

        'owner': owner,

        'accommodations': accommodations,

        'pending_bookings': pending_bookings,

        'confirmed_bookings': confirmed_bookings,

        'checked_in_bookings': checked_in_bookings,

        'pending_count': pending_count,

    })





@login_required

def accommodation_owner_accommodations(request):

    """List owner's accommodations"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    accommodations = owner.accommodations.all()

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/owner_accommodations.html', {

        'owner': owner,

        'accommodations': accommodations,

        'pending_count': pending_count,

    })





@login_required

def add_accommodation(request):

    """Add new accommodation"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    if request.method == 'POST':

        form = AccommodationForm(request.POST, request.FILES)

        if form.is_valid():

            accommodation = form.save(commit=False)

            accommodation.owner = owner

            accommodation.save()

            messages.success(request, 'Accommodation added successfully!')

            return redirect('accommodation_owner_accommodations')

    else:

        form = AccommodationForm()

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/add_accommodation.html', {

        'form': form,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def edit_accommodation(request, pk):

    """Edit accommodation"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    accommodation = get_object_or_404(Accommodation, pk=pk, owner=owner)

    

    if request.method == 'POST':

        form = AccommodationForm(request.POST, request.FILES, instance=accommodation)

        if form.is_valid():

            form.save()

            messages.success(request, 'Accommodation updated successfully!')

            return redirect('accommodation_owner_accommodations')

    else:

        form = AccommodationForm(instance=accommodation)

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/edit_accommodation.html', {

        'form': form,

        'accommodation': accommodation,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def delete_accommodation(request, pk):

    """Delete accommodation"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    accommodation = get_object_or_404(Accommodation, pk=pk, owner=owner)

    

    if request.method == 'POST':

        accommodation.delete()

        messages.success(request, 'Accommodation deleted successfully!')

        return redirect('accommodation_owner_accommodations')

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/delete_accommodation.html', {

        'accommodation': accommodation,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def accommodation_owner_bookings(request):

    """List owner's bookings"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    bookings = AccommodationBooking.objects.filter(accommodation__owner=owner)

    

    status_filter = request.GET.get('status')

    if status_filter:

        bookings = bookings.filter(booking_status=status_filter)

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/owner_bookings.html', {

        'owner': owner,

        'bookings': bookings,

        'status_filter': status_filter,

        'pending_count': pending_count,

    })





@login_required

def manage_accommodation_booking(request, booking_id):

    """Manage a booking (confirm, check-in, check-out, cancel)"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    booking = get_object_or_404(AccommodationBooking, booking_id=booking_id, accommodation__owner=owner)

    

    if request.method == 'POST':

        action = request.POST.get('action')

        remarks = request.POST.get('remarks', '')

        

        if action == 'confirm':

            booking.booking_status = 'confirmed'

            booking.payment_status = 'verified'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Booking confirmed!')

        elif action == 'check_in':

            booking.booking_status = 'checked_in'

            booking.actual_check_in = timezone.now()

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Guest checked in!')

        elif action == 'check_out':

            booking.booking_status = 'checked_out'

            booking.actual_check_out = timezone.now()

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Guest checked out!')

        elif action == 'cancel':

            booking.booking_status = 'cancelled'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Booking cancelled.')

        elif action == 'no_show':

            booking.booking_status = 'no_show'

            booking.owner_remarks = remarks

            booking.save()

            messages.success(request, 'Marked as no-show.')

        

        return redirect('manage_accommodation_booking', booking_id=booking.booking_id)

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/manage_booking.html', {

        'booking': booking,

        'owner': owner,

        'pending_count': pending_count,

    })





@login_required

def accommodation_owner_profile(request):

    """Owner profile settings"""

    try:

        owner = request.user.accommodation_owner_profile

    except AccommodationOwner.DoesNotExist:

        return redirect('accommodation_owner_register')

    

    if request.method == 'POST':

        owner.business_name = request.POST.get('business_name', owner.business_name)

        owner.phone = request.POST.get('phone', owner.phone)

        owner.alternate_phone = request.POST.get('alternate_phone', owner.alternate_phone)

        owner.address = request.POST.get('address', owner.address)

        owner.city = request.POST.get('city', owner.city)

        owner.upi_id = request.POST.get('upi_id', owner.upi_id)

        

        if 'profile_photo' in request.FILES:

            owner.profile_photo = request.FILES['profile_photo']

        if 'qr_code' in request.FILES:

            owner.qr_code = request.FILES['qr_code']

        

        owner.save()

        messages.success(request, 'Profile updated successfully!')

        return redirect('accommodation_owner_profile')

    

    pending_count = AccommodationBooking.objects.filter(

        accommodation__owner=owner,

        booking_status='pending',

        payment_status='submitted'

    ).count()

    

    return render(request, 'accommodations/owner_profile.html', {

        'owner': owner,

        'pending_count': pending_count,

    })

