from django.shortcuts import render,redirect
from . models import MeghalayaImages,MeghalyaVideos,RegionOfMeghalaya, Festival, TrevalAround
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
# def home(request):
#     meghaData = MeghalayaImages.objects.all()
#     return render(request,"website/home.html",{"meghaData":meghaData})

@login_required
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
    return render(request, 'allPlaces.html', {
        "mydata": mydata,
        "mydataVideo": mydataVideo,
        "location": name  # ✅ passing place name for geocoding
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
