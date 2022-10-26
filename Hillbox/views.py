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