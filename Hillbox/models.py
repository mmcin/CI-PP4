from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# this is where I will store the flying sites that user uploads I based this model on the model from the CI blog post with the obvious changes such as adding choices for the wind direction
class FlyingSite(models.Model):

    WIND_CHOICES = (
        ('N', 'N'),
        ('NW', 'NW'),
        ('NE', 'NE'),
        ('S', 'S'),
        ('SE', 'SE'),
        ('SW', 'SW'),
        ('E', 'E'),
        ('W', 'W'),)
    site_name = models.CharField(max_length = 150, unique=True)
    wind_direction = models.CharField(max_length = 150, choices=WIND_CHOICES)
    slug = models.SlugField(max_length=200, unique=True, default = "12345")
    pilot = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flying_sites")
    updated_on = models.DateTimeField(auto_now=True)
    overview = models.TextField()
    landing_information = models.TextField()
    warnings = models.TextField()
    featured_image = CloudinaryField('images', default='placeholder')
    status = models.IntegerField(choices = STATUS, default = 0)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.site_name

# this is where I will store the photos for the gallery
class Photo(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photo")
    site_name = models.CharField(max_length = 150, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices = STATUS, default = 0)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.site_name 

# this is where I will store the comments related to the flying site model
class Comment(models.Model):
    site = models.ForeignKey(FlyingSite, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    name = models.CharField(max_length=100, default="Unknown Pilot")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
    
   