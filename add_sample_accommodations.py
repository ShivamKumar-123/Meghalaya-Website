import os
import sys
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meghalaya.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from django.contrib.auth.models import User
from app.models import AccommodationOwner, Accommodation

def download_image(url):
    """Download image from URL and return as ContentFile"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return ContentFile(response.content)
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def create_sample_accommodations():
    """Create sample accommodation data with Pexels images"""
    
    # Create or get admin user for owner
    admin_user, created = User.objects.get_or_create(
        username='accommodation_admin',
        defaults={
            'email': 'accommodation@meghalaya.com',
            'first_name': 'Accommodation',
            'last_name': 'Admin',
            'is_staff': True
        }
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Created admin user: accommodation_admin")
    
    # Create AccommodationOwner
    owner, created = AccommodationOwner.objects.get_or_create(
        user=admin_user,
        defaults={
            'business_name': 'Meghalaya Stays',
            'owner_name': 'Rajesh Kumar',
            'phone': '9876543210',
            'alternate_phone': '9876543211',
            'email': 'stays@meghalaya.com',
            'address': 'Police Bazaar, Shillong, Meghalaya',
            'city': 'Shillong',
            'is_verified': True
        }
    )
    if created:
        print("Created AccommodationOwner: Meghalaya Stays")
    
    # Pexels images for accommodations (direct image URLs)
    accommodation_data = [
        {
            'accommodation_type': 'hotel',
            'name': 'The Shillong Grand Hotel',
            'room_type': 'deluxe',
            'address': 'Police Bazaar, Near Ward Lake, Shillong',
            'city': 'Shillong',
            'landmark': 'Near Ward Lake',
            'total_rooms': 25,
            'available_rooms': 20,
            'max_guests_per_room': 3,
            'bed_count': 2,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': True,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': True,
            'room_service': True,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 3500.00,
            'extra_person_charge': 500.00,
            'description': 'Experience luxury at The Shillong Grand Hotel, located in the heart of the city. Our deluxe rooms offer stunning views of the surrounding hills, modern amenities, and exceptional service. Perfect for both business and leisure travelers.',
            'house_rules': 'Check-in: 2:00 PM, Check-out: 11:00 AM. No smoking in rooms. Pets not allowed.',
            'cancellation_policy': 'Free cancellation up to 24 hours before check-in. 50% charge for late cancellation.',
            'is_available': True,
            'is_verified': True,
            'is_featured': True,
            'rating': 4.5,
            'images': [
                'https://images.pexels.com/photos/258154/pexels-photo-258154.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/164595/pexels-photo-164595.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'resort',
            'name': 'Cherrapunji Eco Resort',
            'room_type': 'suite',
            'address': 'Sohra, Near Nohkalikai Falls',
            'city': 'Cherrapunji',
            'landmark': 'Near Nohkalikai Falls',
            'total_rooms': 15,
            'available_rooms': 12,
            'max_guests_per_room': 4,
            'bed_count': 2,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': True,
            'room_service': True,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 5500.00,
            'extra_person_charge': 800.00,
            'description': 'Nestled in the clouds of Cherrapunji, our eco-resort offers a unique experience with breathtaking views of the living root bridges and waterfalls. Wake up to misty mornings and enjoy the pristine beauty of nature.',
            'house_rules': 'Check-in: 1:00 PM, Check-out: 11:00 AM. Eco-friendly practices encouraged. No plastic bottles.',
            'cancellation_policy': 'Free cancellation up to 48 hours before check-in. Full charge for no-show.',
            'is_available': True,
            'is_verified': True,
            'is_featured': True,
            'rating': 4.8,
            'images': [
                'https://images.pexels.com/photos/338504/pexels-photo-338504.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/1134176/pexels-photo-1134176.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'homestay',
            'name': 'Mawlynnong Village Homestay',
            'room_type': 'double',
            'address': 'Mawlynnong Village, East Khasi Hills',
            'city': 'Mawlynnong',
            'landmark': 'Asia\'s Cleanest Village',
            'total_rooms': 5,
            'available_rooms': 4,
            'max_guests_per_room': 2,
            'bed_count': 1,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': False,
            'parking_available': True,
            'restaurant_available': False,
            'room_service': False,
            'laundry_service': False,
            'hot_water': True,
            'power_backup': False,
            'cctv': False,
            'price_per_night': 1800.00,
            'extra_person_charge': 300.00,
            'description': 'Experience authentic Khasi hospitality in Asia\'s cleanest village. Our homestay offers traditional bamboo cottages with modern comforts. Enjoy home-cooked local cuisine and immerse yourself in the village culture.',
            'house_rules': 'Check-in: 12:00 PM, Check-out: 10:00 AM. Respect local customs. No loud music after 9 PM.',
            'cancellation_policy': 'Free cancellation up to 24 hours before check-in.',
            'is_available': True,
            'is_verified': True,
            'is_featured': True,
            'rating': 4.7,
            'images': [
                'https://images.pexels.com/photos/2102587/pexels-photo-2102587.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2507010/pexels-photo-2507010.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2440471/pexels-photo-2440471.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'guest_house',
            'name': 'Dawki Riverside Guest House',
            'room_type': 'twin',
            'address': 'Dawki, Near Umngot River',
            'city': 'Dawki',
            'landmark': 'Near Umngot River Boating Point',
            'total_rooms': 10,
            'available_rooms': 8,
            'max_guests_per_room': 2,
            'bed_count': 2,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': True,
            'room_service': True,
            'laundry_service': False,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 2200.00,
            'extra_person_charge': 400.00,
            'description': 'Located on the banks of the crystal-clear Umngot River, our guest house offers stunning views and easy access to boating activities. Perfect for nature lovers and adventure seekers.',
            'house_rules': 'Check-in: 2:00 PM, Check-out: 11:00 AM. Swimming in the river at own risk.',
            'cancellation_policy': 'Free cancellation up to 24 hours before check-in. 30% charge for late cancellation.',
            'is_available': True,
            'is_verified': True,
            'is_featured': False,
            'rating': 4.4,
            'images': [
                'https://images.pexels.com/photos/1579253/pexels-photo-1579253.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2029722/pexels-photo-2029722.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2034335/pexels-photo-2034335.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'cottage',
            'name': 'Pine Valley Cottage',
            'room_type': 'family',
            'address': 'Upper Shillong, Pine Forest Area',
            'city': 'Shillong',
            'landmark': 'Near Shillong Peak',
            'total_rooms': 8,
            'available_rooms': 6,
            'max_guests_per_room': 5,
            'bed_count': 3,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': False,
            'room_service': False,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 4000.00,
            'extra_person_charge': 600.00,
            'description': 'Escape to our cozy cottages nestled among the pine trees. Each cottage offers privacy, warmth, and stunning views of the valley. Ideal for families and groups seeking a peaceful retreat.',
            'house_rules': 'Check-in: 3:00 PM, Check-out: 11:00 AM. Bonfire allowed in designated areas only.',
            'cancellation_policy': 'Free cancellation up to 48 hours before check-in.',
            'is_available': True,
            'is_verified': True,
            'is_featured': True,
            'rating': 4.6,
            'images': [
                'https://images.pexels.com/photos/803975/pexels-photo-803975.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/1643383/pexels-photo-1643383.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2662116/pexels-photo-2662116.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'hostel',
            'name': 'Backpackers Hub Shillong',
            'room_type': 'dormitory',
            'address': 'Laitumkhrah, Near Don Bosco Square',
            'city': 'Shillong',
            'landmark': 'Near Don Bosco Square',
            'total_rooms': 20,
            'available_rooms': 18,
            'max_guests_per_room': 6,
            'bed_count': 6,
            'bathroom_attached': False,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': True,
            'parking_available': False,
            'restaurant_available': False,
            'room_service': False,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 600.00,
            'extra_person_charge': 0.00,
            'description': 'Budget-friendly hostel perfect for solo travelers and backpackers. Meet fellow travelers, share stories, and explore Meghalaya together. Common kitchen and lounge area available.',
            'house_rules': 'Check-in: 12:00 PM, Check-out: 10:00 AM. Quiet hours after 11 PM. No alcohol in common areas.',
            'cancellation_policy': 'Free cancellation up to 12 hours before check-in.',
            'is_available': True,
            'is_verified': True,
            'is_featured': False,
            'rating': 4.2,
            'images': [
                'https://images.pexels.com/photos/271618/pexels-photo-271618.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/279746/pexels-photo-279746.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/237371/pexels-photo-237371.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'lodge',
            'name': 'Tura Mountain Lodge',
            'room_type': 'double',
            'address': 'Tura, Near Nokrek Peak',
            'city': 'Tura',
            'landmark': 'Gateway to Nokrek National Park',
            'total_rooms': 12,
            'available_rooms': 10,
            'max_guests_per_room': 2,
            'bed_count': 1,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': False,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': True,
            'room_service': True,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 2800.00,
            'extra_person_charge': 500.00,
            'description': 'Your base camp for exploring the Garo Hills. Our lodge offers comfortable rooms with mountain views, local Garo cuisine, and guided tours to Nokrek National Park and surrounding attractions.',
            'house_rules': 'Check-in: 2:00 PM, Check-out: 11:00 AM. Trekking gear available for rent.',
            'cancellation_policy': 'Free cancellation up to 24 hours before check-in.',
            'is_available': True,
            'is_verified': True,
            'is_featured': False,
            'rating': 4.3,
            'images': [
                'https://images.pexels.com/photos/2506923/pexels-photo-2506923.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2373201/pexels-photo-2373201.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2417842/pexels-photo-2417842.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
        {
            'accommodation_type': 'apartment',
            'name': 'Shillong City Apartment',
            'room_type': 'suite',
            'address': 'Lachumiere, Central Shillong',
            'city': 'Shillong',
            'landmark': 'Near State Central Library',
            'total_rooms': 6,
            'available_rooms': 5,
            'max_guests_per_room': 4,
            'bed_count': 2,
            'bathroom_attached': True,
            'wifi_available': True,
            'ac_available': True,
            'tv_available': True,
            'parking_available': True,
            'restaurant_available': False,
            'room_service': False,
            'laundry_service': True,
            'hot_water': True,
            'power_backup': True,
            'cctv': True,
            'price_per_night': 3200.00,
            'extra_person_charge': 500.00,
            'description': 'Fully furnished apartment in the heart of Shillong. Features a living room, kitchenette, and bedroom. Perfect for extended stays and families who prefer a home-like experience.',
            'house_rules': 'Check-in: 2:00 PM, Check-out: 11:00 AM. Self-catering. Cleaning service twice a week.',
            'cancellation_policy': 'Free cancellation up to 48 hours before check-in. 25% charge for late cancellation.',
            'is_available': True,
            'is_verified': True,
            'is_featured': False,
            'rating': 4.4,
            'images': [
                'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg?auto=compress&cs=tinysrgb&w=800',
                'https://images.pexels.com/photos/2062431/pexels-photo-2062431.jpeg?auto=compress&cs=tinysrgb&w=800',
            ]
        },
    ]
    
    created_count = 0
    for data in accommodation_data:
        # Check if accommodation already exists
        if Accommodation.objects.filter(name=data['name']).exists():
            print(f"Accommodation '{data['name']}' already exists, skipping...")
            continue
        
        images = data.pop('images')
        
        # Create accommodation
        accommodation = Accommodation(owner=owner, **data)
        
        # Download and save images
        for i, img_url in enumerate(images):
            img_content = download_image(img_url)
            if img_content:
                field_name = f'photo_{i+1}'
                filename = f"{data['name'].replace(' ', '_').lower()}_{i+1}.jpg"
                getattr(accommodation, field_name).save(filename, img_content, save=False)
                print(f"  Downloaded image {i+1} for {data['name']}")
        
        accommodation.save()
        created_count += 1
        print(f"Created: {accommodation.name}")
    
    print(f"\nTotal accommodations created: {created_count}")
    print(f"Total accommodations in database: {Accommodation.objects.count()}")

if __name__ == '__main__':
    print("Creating sample accommodation data...")
    create_sample_accommodations()
    print("\nDone!")
