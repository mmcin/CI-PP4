from .models import Comment, PhotoComment, FlyingSite, Photo
from django import forms

# this is the upload form for flying sites
class SiteUpload(forms.ModelForm):
    class Meta:
        model = FlyingSite
        fields = ('site_name', 'wind_direction', 'overview', 'landing_information', 'warnings', 'featured_image', 'status', 'slug')

# this is the form to upload a gallery images
class GalleryUpload(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('featured_image', 'site_name', 'status', 'slug')

# this is the form to comment on a flying site
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)

# this is the form to comment on a gallery image
class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('body',)
