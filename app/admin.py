from django.contrib import admin
from . models import MeghalayaImages,MeghalyaVideos,RegionOfMeghalaya,TrevalAround,Festival

# Register your models here.
class MeghalayaImageAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)


class MeghalyaVideosAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)


class RegionOfMeghalayaAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","updated_at")

class FestivalOfMeghalayaAdmin(admin.ModelAdmin):
    list_display = ("festival_name","created_at","updated_at")


class TrevalAroundAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)



admin.site.register(TrevalAround, TrevalAroundAdmin)
admin.site.register(Festival,FestivalOfMeghalayaAdmin)
admin.site.register(RegionOfMeghalaya, RegionOfMeghalayaAdmin)
admin.site.register(MeghalayaImages, MeghalayaImageAdmin)
admin.site.register(MeghalyaVideos, MeghalyaVideosAdmin)