from django.views import generic, View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import FlyingSite, Photo, Comment, PhotoComment
from .forms import CommentForm, PhotoCommentForm, ContactForm, SiteUpload, GalleryUpload
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

import os
if os.path.isfile('env.py'):
    import env

# this view returns the homepage
def index(request):
    return render(
        request,
        "index.html",
    )

# displays the error page when user doesn't have permissions
def NotAuthorised(request):
    return render(
        request,
        "not_authorised.html",
    )

# displays the uploaded flying sites 
class SiteList(generic.ListView):
    model = FlyingSite
    queryset = FlyingSite.objects.filter(status=1).order_by('-updated_on')
    template_name = 'site_list.html'
    paginate_by = 8

# displays the images on the gallery page
class PhotoList(generic.ListView):
    model = Photo
    queryset = Photo.objects.filter(status=1).order_by('-updated_on')
    template_name = 'gallery.html'
    paginate_by = 8

# uploads a new flying site
def UploadFlyingSite(request):
    site_form = SiteUpload(request.POST, request.FILES)
    if request.method == "POST":
        if site_form.is_valid():
            site_form.instance.pilot = request.user
            site_done = site_form.save(commit=False)
            site_done.save()
        return HttpResponseRedirect('/sites')
        
    return render(request, 'site_upload.html', {'form': site_form})  

# edit a site in flyingsite model
def EditSite(request, site_id):
    site = get_object_or_404(FlyingSite, id = site_id)
    form = SiteUpload(instance = site)
    if request.user == site.pilot:
        if request.method == "POST":
            form = SiteUpload(request.POST, request.FILES, instance = site)
            if form.is_valid():
                form.save(commit=False)
                form.save()
            return HttpResponseRedirect('/sites')
    else: 
        return redirect('not_authorised')

    return render(request, 'site_edit.html', {'form': form})  

# delete a site in flyingsite model
def DeleteSite(request, site_id):
    site = get_object_or_404(FlyingSite, id = site_id)
    form = SiteUpload(instance = site)
    if request.user == site.pilot:
        if request.method == "POST":
            form = SiteUpload(request.POST, instance = site)
            site.delete()
            return HttpResponseRedirect('/sites')
    else:
        return redirect('not_authorised')
    return render(request, 'site_delete.html', {'form': form})