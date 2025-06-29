from django.urls import path
from . import views

urlpatterns = [
    # Main route handled by app
    # Add more app-specific routes here if needed
    path('register/',views.register,name="register"),
    path('', views.home, name="home"),
    path('place/<str:name>/',views.allPlaces,name="allPlace"),
    
    # path('login/',views.login,name="login"),
    # path('logout/',views.logout,name="logout")
    path('regionOfMeghalaya/<str:name>/',views.regionMeghalaya,name="regionOfMeghalay"),
    path('festivalOfMeghalaya/<str:festival_name>/',views.festivalMeghalaya,name="festivalsOfMeghalaya"),
    path('trevalAround/<str:name>/',views.trevalAroundMeghalaya,name="trevalAroundOfMeghalaya"),
]
