from .models import MeghalayaImages

def navbar_context(request):
    """
    Context processor to make placeName available in all templates
    for the navbar dropdown
    """
    placeName = MeghalayaImages.objects.values('name').exclude(
        name__in=["Cherrapunji", "Police Bazar", "Seven Sister Falls", "Dawki River", "Cathedral of Mary"]
    ).distinct()
    
    return {
        'placeName': placeName
    }
