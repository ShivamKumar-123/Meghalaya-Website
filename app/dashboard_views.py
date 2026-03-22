from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    MeghalayaLocation, RegionOfMeghalaya, Festival, 
    MeghalayaImages, MeghalyaVideos, TrevalAround,
    ContactMessage, MessageReply
)

def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser

# Dashboard Home
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_home(request):
    context = {
        'places_count': MeghalayaLocation.objects.count(),
        'regions_count': RegionOfMeghalaya.objects.count(),
        'festivals_count': Festival.objects.count(),
        'users_count': User.objects.count(),
        'recent_places': MeghalayaLocation.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/dashboard_home.html', context)

# ==================== PLACES CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_places(request):
    places = MeghalayaLocation.objects.all().order_by('-created_at')
    return render(request, 'dashboard/places_list.html', {'places': places})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_places_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        placeUrl = request.POST.get('placeUrl', '')
        
        MeghalayaLocation.objects.create(name=name, placeUrl=placeUrl)
        messages.success(request, f'Place "{name}" added successfully!')
        return redirect('dashboard_places')
    
    return render(request, 'dashboard/places_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_places_edit(request, pk):
    place = get_object_or_404(MeghalayaLocation, pk=pk)
    
    if request.method == 'POST':
        place.name = request.POST.get('name')
        place.placeUrl = request.POST.get('placeUrl', '')
        place.save()
        messages.success(request, f'Place "{place.name}" updated successfully!')
        return redirect('dashboard_places')
    
    return render(request, 'dashboard/places_form.html', {'place': place})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_places_delete(request, pk):
    place = get_object_or_404(MeghalayaLocation, pk=pk)
    name = place.name
    place.delete()
    messages.success(request, f'Place "{name}" deleted successfully!')
    return redirect('dashboard_places')

# ==================== REGIONS CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_regions(request):
    regions = RegionOfMeghalaya.objects.all().order_by('-created_at')
    return render(request, 'dashboard/regions_list.html', {'regions': regions})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_regions_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        region_name = request.POST.get('region_name', '')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        
        RegionOfMeghalaya.objects.create(
            name=name,
            region_name=region_name,
            description=description,
            image=image
        )
        messages.success(request, f'Region "{name}" added successfully!')
        return redirect('dashboard_regions')
    
    return render(request, 'dashboard/regions_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_regions_edit(request, pk):
    region = get_object_or_404(RegionOfMeghalaya, pk=pk)
    
    if request.method == 'POST':
        region.name = request.POST.get('name')
        region.region_name = request.POST.get('region_name', '')
        region.description = request.POST.get('description', '')
        if request.FILES.get('image'):
            region.image = request.FILES.get('image')
        region.save()
        messages.success(request, f'Region "{region.name}" updated successfully!')
        return redirect('dashboard_regions')
    
    return render(request, 'dashboard/regions_form.html', {'region': region})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_regions_delete(request, pk):
    region = get_object_or_404(RegionOfMeghalaya, pk=pk)
    name = region.name
    region.delete()
    messages.success(request, f'Region "{name}" deleted successfully!')
    return redirect('dashboard_regions')

# ==================== FESTIVALS CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_festivals(request):
    festivals = Festival.objects.all().order_by('-created_at')
    return render(request, 'dashboard/festivals_list.html', {'festivals': festivals})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_festivals_add(request):
    if request.method == 'POST':
        festival_name = request.POST.get('festival_name')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        
        Festival.objects.create(
            festival_name=festival_name,
            description=description,
            image=image
        )
        messages.success(request, f'Festival "{festival_name}" added successfully!')
        return redirect('dashboard_festivals')
    
    return render(request, 'dashboard/festivals_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_festivals_edit(request, pk):
    festival = get_object_or_404(Festival, pk=pk)
    
    if request.method == 'POST':
        festival.festival_name = request.POST.get('festival_name')
        festival.description = request.POST.get('description', '')
        if request.FILES.get('image'):
            festival.image = request.FILES.get('image')
        festival.save()
        messages.success(request, f'Festival "{festival.festival_name}" updated successfully!')
        return redirect('dashboard_festivals')
    
    return render(request, 'dashboard/festivals_form.html', {'festival': festival})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_festivals_delete(request, pk):
    festival = get_object_or_404(Festival, pk=pk)
    name = festival.festival_name
    festival.delete()
    messages.success(request, f'Festival "{name}" deleted successfully!')
    return redirect('dashboard_festivals')

# ==================== IMAGES CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_images(request):
    images = MeghalayaImages.objects.all().order_by('-created_at')
    return render(request, 'dashboard/images_list.html', {'images': images})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_images_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        
        MeghalayaImages.objects.create(
            name=name,
            description=description,
            image=image
        )
        messages.success(request, f'Image "{name}" uploaded successfully!')
        return redirect('dashboard_images')
    
    return render(request, 'dashboard/images_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_images_edit(request, pk):
    image = get_object_or_404(MeghalayaImages, pk=pk)
    
    if request.method == 'POST':
        image.name = request.POST.get('name')
        image.description = request.POST.get('description', '')
        if request.FILES.get('image'):
            image.image = request.FILES.get('image')
        image.save()
        messages.success(request, f'Image "{image.name}" updated successfully!')
        return redirect('dashboard_images')
    
    return render(request, 'dashboard/images_form.html', {'image': image})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_images_delete(request, pk):
    image = get_object_or_404(MeghalayaImages, pk=pk)
    name = image.name
    image.delete()
    messages.success(request, f'Image "{name}" deleted successfully!')
    return redirect('dashboard_images')

# ==================== VIDEOS CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_videos(request):
    videos = MeghalyaVideos.objects.all().order_by('-created_at')
    return render(request, 'dashboard/videos_list.html', {'videos': videos})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_videos_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        video = request.FILES.get('video')
        
        MeghalyaVideos.objects.create(
            name=name,
            description=description,
            video=video
        )
        messages.success(request, f'Video "{name}" uploaded successfully!')
        return redirect('dashboard_videos')
    
    return render(request, 'dashboard/videos_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_videos_edit(request, pk):
    video = get_object_or_404(MeghalyaVideos, pk=pk)
    
    if request.method == 'POST':
        video.name = request.POST.get('name')
        video.description = request.POST.get('description', '')
        if request.FILES.get('video'):
            video.video = request.FILES.get('video')
        video.save()
        messages.success(request, f'Video "{video.name}" updated successfully!')
        return redirect('dashboard_videos')
    
    return render(request, 'dashboard/videos_form.html', {'video': video})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_videos_delete(request, pk):
    video = get_object_or_404(MeghalyaVideos, pk=pk)
    name = video.name
    video.delete()
    messages.success(request, f'Video "{name}" deleted successfully!')
    return redirect('dashboard_videos')

# ==================== TRAVEL AROUND CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_travel(request):
    travels = TrevalAround.objects.all().order_by('-created_at')
    return render(request, 'dashboard/travel_list.html', {'travels': travels})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_travel_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        
        TrevalAround.objects.create(
            name=name,
            place=place,
            description=description,
            image=image
        )
        messages.success(request, f'Travel "{name}" added successfully!')
        return redirect('dashboard_travel')
    
    return render(request, 'dashboard/travel_form.html')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_travel_edit(request, pk):
    travel = get_object_or_404(TrevalAround, pk=pk)
    
    if request.method == 'POST':
        travel.name = request.POST.get('name')
        travel.place = request.POST.get('place')
        travel.description = request.POST.get('description', '')
        if request.FILES.get('image'):
            travel.image = request.FILES.get('image')
        travel.save()
        messages.success(request, f'Travel "{travel.name}" updated successfully!')
        return redirect('dashboard_travel')
    
    return render(request, 'dashboard/travel_form.html', {'travel': travel})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_travel_delete(request, pk):
    travel = get_object_or_404(TrevalAround, pk=pk)
    name = travel.name
    travel.delete()
    messages.success(request, f'Travel "{name}" deleted successfully!')
    return redirect('dashboard_travel')

# ==================== USERS LIST ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_users(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'dashboard/users_list.html', {'users': users})


# ==================== MESSAGES CRUD ====================
@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_messages(request):
    status_filter = request.GET.get('status', '')
    messages_list = ContactMessage.objects.all()
    
    if status_filter:
        messages_list = messages_list.filter(status=status_filter)
    
    unread_count = ContactMessage.objects.filter(status='unread').count()
    
    return render(request, 'dashboard/messages_list.html', {
        'messages_list': messages_list,
        'status_filter': status_filter,
        'unread_count': unread_count,
    })


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_message_detail(request, pk):
    contact_message = get_object_or_404(ContactMessage, pk=pk)
    
    # Mark as read if unread
    if contact_message.status == 'unread':
        contact_message.status = 'read'
        contact_message.save()
    
    # Handle reply submission
    if request.method == 'POST':
        reply_text = request.POST.get('reply_text')
        if reply_text:
            MessageReply.objects.create(
                message=contact_message,
                user=request.user,
                reply_text=reply_text,
                is_admin_reply=True
            )
            contact_message.status = 'replied'
            contact_message.save()
            
            # Send email notification to user
            try:
                send_mail(
                    f'Re: {contact_message.get_subject_display()} - Meghalaya Tourism',
                    f"Dear {contact_message.name},\n\nThank you for contacting us. Here is our response:\n\n{reply_text}\n\nBest regards,\nMeghalaya Tourism Team",
                    settings.EMAIL_HOST_USER,
                    [contact_message.email],
                    fail_silently=True,
                )
            except:
                pass
            
            messages.success(request, 'Reply sent successfully!')
            return redirect('dashboard_message_detail', pk=pk)
    
    replies = contact_message.replies.all()
    
    return render(request, 'dashboard/message_detail.html', {
        'contact_message': contact_message,
        'replies': replies,
    })


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_message_status(request, pk):
    contact_message = get_object_or_404(ContactMessage, pk=pk)
    new_status = request.GET.get('status', 'read')
    
    if new_status in ['unread', 'read', 'replied', 'closed']:
        contact_message.status = new_status
        contact_message.save()
        messages.success(request, f'Message status updated to {new_status}!')
    
    return redirect('dashboard_messages')


@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_message_delete(request, pk):
    contact_message = get_object_or_404(ContactMessage, pk=pk)
    contact_message.delete()
    messages.success(request, 'Message deleted successfully!')
    return redirect('dashboard_messages')


# ==================== VEHICLE BOOKING MANAGEMENT ====================
from .models import VehicleOwner, Vehicle, VehicleBooking

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_vehicle_owners(request):
    owners = VehicleOwner.objects.all().order_by('-created_at')
    return render(request, 'dashboard/vehicle_owners.html', {'owners': owners})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_vehicle_owner_verify(request, pk):
    owner = get_object_or_404(VehicleOwner, pk=pk)
    action = request.GET.get('action', 'verify')
    
    if action == 'verify':
        owner.is_verified = True
        owner.save()
        messages.success(request, f'Vehicle owner "{owner.business_name}" verified!')
    elif action == 'unverify':
        owner.is_verified = False
        owner.save()
        messages.warning(request, f'Vehicle owner "{owner.business_name}" unverified!')
    elif action == 'activate':
        owner.is_active = True
        owner.save()
        messages.success(request, f'Vehicle owner "{owner.business_name}" activated!')
    elif action == 'deactivate':
        owner.is_active = False
        owner.save()
        messages.warning(request, f'Vehicle owner "{owner.business_name}" deactivated!')
    
    return redirect('dashboard_vehicle_owners')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_vehicles(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    return render(request, 'dashboard/vehicles_list.html', {'vehicles': vehicles})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_vehicle_verify(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    action = request.GET.get('action', 'verify')
    
    if action == 'verify':
        vehicle.is_verified = True
        vehicle.save()
        messages.success(request, f'Vehicle "{vehicle.vehicle_name}" verified!')
    elif action == 'unverify':
        vehicle.is_verified = False
        vehicle.save()
        messages.warning(request, f'Vehicle "{vehicle.vehicle_name}" unverified!')
    
    return redirect('dashboard_vehicles')

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_bookings(request):
    bookings = VehicleBooking.objects.all().order_by('-created_at')
    return render(request, 'dashboard/bookings_list.html', {'bookings': bookings})

@login_required
@user_passes_test(is_staff_or_superuser)
def dashboard_booking_detail(request, booking_id):
    booking = get_object_or_404(VehicleBooking, booking_id=booking_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm':
            booking.booking_status = 'confirmed'
            booking.payment_status = 'verified'
            booking.save()
            messages.success(request, 'Booking confirmed!')
        elif action == 'cancel':
            booking.booking_status = 'cancelled'
            booking.save()
            messages.warning(request, 'Booking cancelled!')
        return redirect('dashboard_bookings')
    
    return render(request, 'dashboard/booking_detail.html', {'booking': booking})
