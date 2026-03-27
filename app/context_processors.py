from django.core.cache import cache
from .models import MeghalayaImages

def navbar_context(request):
    """
    Context processor to make placeName available in all templates
    for the navbar dropdown. Uses caching to avoid database query on every request.
    """
    # Try to get from cache first
    placeName = cache.get('navbar_places')
    
    if placeName is None:
        # Query database and cache for 5 minutes (300 seconds)
        placeName = list(MeghalayaImages.objects.values('name').exclude(
            name__in=["Cherrapunji", "Police Bazar", "Seven Sister Falls", "Dawki River", "Cathedral of Mary"]
        ).distinct())
        cache.set('navbar_places', placeName, 300)
    
    return {
        'placeName': placeName
    }
