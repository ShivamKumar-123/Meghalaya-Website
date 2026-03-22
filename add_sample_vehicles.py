"""
Script to add sample vehicle owners and vehicles to the database
Run with: python manage.py shell < add_sample_vehicles.py
"""
import os
import django
import requests
from io import BytesIO
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meghalaya.settings')
django.setup()

from django.contrib.auth.models import User
from app.models import VehicleOwner, Vehicle

# Pexels image URLs for different vehicle types
VEHICLE_IMAGES = {
    'rickshaw': 'https://images.pexels.com/photos/2224861/pexels-photo-2224861.jpeg?auto=compress&cs=tinysrgb&w=800',
    'taxi': 'https://images.pexels.com/photos/2526127/pexels-photo-2526127.jpeg?auto=compress&cs=tinysrgb&w=800',
    'car': 'https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&w=800',
    'bus': 'https://images.pexels.com/photos/68547/pexels-photo-68547.jpeg?auto=compress&cs=tinysrgb&w=800',
    'bike': 'https://images.pexels.com/photos/2519374/pexels-photo-2519374.jpeg?auto=compress&cs=tinysrgb&w=800',
}

# Additional vehicle images
EXTRA_IMAGES = {
    'suv': 'https://images.pexels.com/photos/116675/pexels-photo-116675.jpeg?auto=compress&cs=tinysrgb&w=800',
    'sedan': 'https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg?auto=compress&cs=tinysrgb&w=800',
    'minibus': 'https://images.pexels.com/photos/1178448/pexels-photo-1178448.jpeg?auto=compress&cs=tinysrgb&w=800',
    'scooter': 'https://images.pexels.com/photos/2549941/pexels-photo-2549941.jpeg?auto=compress&cs=tinysrgb&w=800',
    'auto': 'https://images.pexels.com/photos/3422053/pexels-photo-3422053.jpeg?auto=compress&cs=tinysrgb&w=800',
}

# Owner profile images
OWNER_IMAGES = [
    'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg?auto=compress&cs=tinysrgb&w=400',
    'https://images.pexels.com/photos/1222271/pexels-photo-1222271.jpeg?auto=compress&cs=tinysrgb&w=400',
    'https://images.pexels.com/photos/614810/pexels-photo-614810.jpeg?auto=compress&cs=tinysrgb&w=400',
    'https://images.pexels.com/photos/1043471/pexels-photo-1043471.jpeg?auto=compress&cs=tinysrgb&w=400',
    'https://images.pexels.com/photos/91227/pexels-photo-91227.jpeg?auto=compress&cs=tinysrgb&w=400',
]

def download_image(url, filename):
    """Download image from URL and return ContentFile"""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return ContentFile(response.content, name=filename)
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return None

# Sample vehicle owners data
OWNERS_DATA = [
    {
        'business_name': 'Shillong City Cabs',
        'owner_name': 'Rajesh Khongsit',
        'email': 'rajesh.cabs@example.com',
        'phone': '9856123456',
        'alt_phone': '8974561230',
        'address': 'Police Bazar, Shillong',
        'city': 'Shillong',
        'state': 'Meghalaya',
        'pincode': '793001',
        'upi_id': 'rajeshcabs@upi',
        'vehicles': [
            {
                'category': 'taxi',
                'vehicle_name': 'Swift Dzire',
                'vehicle_number': 'ML-05-A-1234',
                'vehicle_model': 'Maruti Suzuki Swift Dzire 2022',
                'seating_capacity': 4,
                'fuel_type': 'petrol',
                'ac_available': True,
                'base_fare': 500,
                'price_per_km': 12,
                'description': 'Comfortable sedan perfect for city tours and airport transfers. AC, music system, and clean interiors.',
            },
            {
                'category': 'car',
                'vehicle_name': 'Innova Crysta',
                'vehicle_number': 'ML-05-B-5678',
                'vehicle_model': 'Toyota Innova Crysta 2023',
                'seating_capacity': 7,
                'fuel_type': 'diesel',
                'ac_available': True,
                'base_fare': 1200,
                'price_per_km': 18,
                'description': 'Premium SUV for family trips and group tours. Spacious, comfortable with ample luggage space.',
            }
        ]
    },
    {
        'business_name': 'Cherrapunji Tours',
        'owner_name': 'David Lyngdoh',
        'email': 'david.tours@example.com',
        'phone': '9863214567',
        'alt_phone': '',
        'address': 'Main Road, Cherrapunji',
        'city': 'Cherrapunji',
        'state': 'Meghalaya',
        'pincode': '793108',
        'upi_id': 'davidtours@paytm',
        'vehicles': [
            {
                'category': 'car',
                'vehicle_name': 'Mahindra Scorpio',
                'vehicle_number': 'ML-07-C-9012',
                'vehicle_model': 'Mahindra Scorpio N 2023',
                'seating_capacity': 7,
                'fuel_type': 'diesel',
                'ac_available': True,
                'base_fare': 1000,
                'price_per_km': 15,
                'description': 'Rugged SUV perfect for hill terrain. Ideal for Cherrapunji and Mawsynram trips.',
            }
        ]
    },
    {
        'business_name': 'Megha Auto Service',
        'owner_name': 'Bah Kynmaw',
        'email': 'megha.auto@example.com',
        'phone': '8794561234',
        'alt_phone': '9876543210',
        'address': 'Bara Bazar, Shillong',
        'city': 'Shillong',
        'state': 'Meghalaya',
        'pincode': '793001',
        'upi_id': 'meghaauto@gpay',
        'vehicles': [
            {
                'category': 'rickshaw',
                'vehicle_name': 'City Auto',
                'vehicle_number': 'ML-05-AU-3456',
                'vehicle_model': 'Bajaj RE 2021',
                'seating_capacity': 3,
                'fuel_type': 'cng',
                'ac_available': False,
                'base_fare': 50,
                'price_per_km': 8,
                'description': 'Affordable auto rickshaw for short city rides. Quick and economical.',
            },
            {
                'category': 'rickshaw',
                'vehicle_name': 'Express Auto',
                'vehicle_number': 'ML-05-AU-7890',
                'vehicle_model': 'Piaggio Ape 2022',
                'seating_capacity': 3,
                'fuel_type': 'petrol',
                'ac_available': False,
                'base_fare': 60,
                'price_per_km': 9,
                'description': 'Fast and reliable auto service. Best for market visits and short trips.',
            }
        ]
    },
    {
        'business_name': 'Northeast Bus Services',
        'owner_name': 'Phibakordor Syiem',
        'email': 'nebusservices@example.com',
        'phone': '9612345678',
        'alt_phone': '8901234567',
        'address': 'MG Road, Shillong',
        'city': 'Shillong',
        'state': 'Meghalaya',
        'pincode': '793001',
        'upi_id': 'nebus@phonepe',
        'vehicles': [
            {
                'category': 'bus',
                'vehicle_name': 'Tourist Mini Bus',
                'vehicle_number': 'ML-05-T-1122',
                'vehicle_model': 'Force Traveller 2022',
                'seating_capacity': 12,
                'fuel_type': 'diesel',
                'ac_available': True,
                'base_fare': 3000,
                'price_per_km': 25,
                'description': 'AC mini bus perfect for group tours. Comfortable seating with luggage carrier.',
            },
            {
                'category': 'bus',
                'vehicle_name': 'Luxury Coach',
                'vehicle_number': 'ML-05-T-3344',
                'vehicle_model': 'Tempo Traveller 2023',
                'seating_capacity': 17,
                'fuel_type': 'diesel',
                'ac_available': True,
                'base_fare': 5000,
                'price_per_km': 35,
                'description': 'Premium luxury coach with pushback seats, AC, and entertainment system.',
            }
        ]
    },
    {
        'business_name': 'Ride Easy Bikes',
        'owner_name': 'Banraplang Marwein',
        'email': 'rideeasy@example.com',
        'phone': '7896541230',
        'alt_phone': '',
        'address': 'Laitumkhrah, Shillong',
        'city': 'Shillong',
        'state': 'Meghalaya',
        'pincode': '793003',
        'upi_id': 'rideeasy@upi',
        'vehicles': [
            {
                'category': 'bike',
                'vehicle_name': 'Royal Enfield Classic',
                'vehicle_number': 'ML-05-E-5566',
                'vehicle_model': 'Royal Enfield Classic 350 2023',
                'seating_capacity': 2,
                'fuel_type': 'petrol',
                'ac_available': False,
                'base_fare': 300,
                'price_per_km': 5,
                'description': 'Iconic bike for exploring scenic routes. Perfect for adventure seekers.',
            },
            {
                'category': 'bike',
                'vehicle_name': 'Honda Activa',
                'vehicle_number': 'ML-05-S-7788',
                'vehicle_model': 'Honda Activa 6G 2023',
                'seating_capacity': 2,
                'fuel_type': 'petrol',
                'ac_available': False,
                'base_fare': 150,
                'price_per_km': 3,
                'description': 'Easy to ride scooter for city exploration. Fuel efficient and comfortable.',
            }
        ]
    }
]

def create_sample_data():
    print("Creating sample vehicle owners and vehicles...")
    
    # Get or create admin user for owners without accounts
    admin_user, _ = User.objects.get_or_create(
        username='vehicle_admin',
        defaults={
            'email': 'vehicle_admin@example.com',
            'is_staff': False,
        }
    )
    
    image_index = 0
    vehicle_images_list = list(VEHICLE_IMAGES.values()) + list(EXTRA_IMAGES.values())
    
    for i, owner_data in enumerate(OWNERS_DATA):
        # Check if owner already exists
        if VehicleOwner.objects.filter(email=owner_data['email']).exists():
            print(f"Owner {owner_data['business_name']} already exists, skipping...")
            continue
        
        # Create user for owner
        username = owner_data['email'].split('@')[0]
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': owner_data['email'],
                'first_name': owner_data['owner_name'].split()[0],
                'last_name': ' '.join(owner_data['owner_name'].split()[1:]),
            }
        )
        if created:
            user.set_password('password123')
            user.save()
        
        # Download owner profile image
        owner_photo = download_image(OWNER_IMAGES[i], f"owner_{i+1}.jpg")
        
        # Create vehicle owner
        owner = VehicleOwner.objects.create(
            user=user,
            business_name=owner_data['business_name'],
            owner_name=owner_data['owner_name'],
            email=owner_data['email'],
            phone=owner_data['phone'],
            alternate_phone=owner_data['alt_phone'] if owner_data['alt_phone'] else None,
            address=owner_data['address'],
            city=owner_data['city'],
            upi_id=owner_data['upi_id'],
            is_verified=True,
            is_active=True,
        )
        
        if owner_photo:
            owner.profile_photo.save(f"owner_{i+1}.jpg", owner_photo)
        
        print(f"Created owner: {owner.business_name}")
        
        # Create vehicles for this owner
        for j, vehicle_data in enumerate(owner_data['vehicles']):
            # Get appropriate image based on category
            category = vehicle_data['category']
            if category in VEHICLE_IMAGES:
                img_url = VEHICLE_IMAGES[category]
            else:
                img_url = vehicle_images_list[image_index % len(vehicle_images_list)]
                image_index += 1
            
            vehicle_photo = download_image(img_url, f"vehicle_{owner.id}_{j+1}.jpg")
            
            vehicle = Vehicle.objects.create(
                owner=owner,
                category=vehicle_data['category'],
                vehicle_name=vehicle_data['vehicle_name'],
                vehicle_number=vehicle_data['vehicle_number'],
                vehicle_model=vehicle_data['vehicle_model'],
                seating_capacity=vehicle_data['seating_capacity'],
                fuel_type=vehicle_data['fuel_type'],
                ac_available=vehicle_data['ac_available'],
                base_fare=vehicle_data['base_fare'],
                price_per_km=vehicle_data['price_per_km'],
                description=vehicle_data['description'],
                is_available=True,
                is_verified=True,
            )
            
            if vehicle_photo:
                vehicle.vehicle_photo_1.save(f"vehicle_{owner.id}_{j+1}.jpg", vehicle_photo)
            
            print(f"  - Created vehicle: {vehicle.vehicle_name} ({vehicle.get_category_display()})")
    
    print("\nDone! Sample data created successfully.")
    print(f"Total Vehicle Owners: {VehicleOwner.objects.count()}")
    print(f"Total Vehicles: {Vehicle.objects.count()}")

if __name__ == '__main__':
    create_sample_data()
