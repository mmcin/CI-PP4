from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FlyingSite, Comment, Photo, PhotoComment

# this is the admin for the FlyingSite 
models@admin.register(FlyingSite)
class FlyingSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}
    actions = ['approve_sites']
    list_display = ('site_name', 'updated_on', 'approved', 'pilot')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')
    
    def approve_flying_sites(self, request, queryset):
        queryset.update(approved=True)

# this id the admin for the gallery images/photos
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}
    actions = ['approve_photos']
    list_display = ('site_name', 'updated_on', 'approved')
    search_fields = ['site_name', 'wind_direction']
    list_filter = ('approved', 'updated_on')
    
    def approve_photos(self, request, queryset):
        queryset.update(approved=True)