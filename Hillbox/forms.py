from .models import Comment, PhotoComment, FlyingSite, Photo
from django import forms

# this is the upload form for flying sites
class SiteUpload(forms.ModelForm):
    class Meta:
        model = FlyingSite
        fields = ('site_name', 'wind_direction', 'overview', 'landing_information', 'warnings', 'featured_image', 'status', 'slug')