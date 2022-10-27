from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_authorised', views.NotAuthorised, name='not_authorised'),
    path('sites/', views.SiteList.as_view(), name='sites'),
    path('gallery/', views.PhotoList.as_view(), name='gallery'),
    path('gallery/<slug:slug>/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('gallery_upload/', views.UploadGalleryImage, name='gallery_upload'),
    path('gallery/delete/<uploaded_by>/<photo_id>', views.DeleteGallery, name='delete_gallery'),
    path('gallery/edit/<uploaded_by>/<photo_id>', views.EditGallery, name='edit_gallery'),
    path('photo_comment_edit/<comment_id>', views.EditPhotoComment, name='photo_comment_edit'),
    path('photo_comment_delete/<comment_id>', views.DeletePhotoComment, name='photo_comment_delete'),
    path('edit/<site_id>', views.EditSite, name='edit'),
    path('delete/<site_id>', views.DeleteSite, name='delete'),
    path('sites/<slug:site_name>/', views.SiteDetail.as_view(), name='site_detail'),
    path('site_upload/', views.UploadFlyingSite, name='site_upload'),
    path('site_comment_edit/<comment_id>', views.EditComment, name='site_comment_edit'),
    path('site_comment_delete/<comment_id>', views.DeleteComment, name='site_comment_delete'),
    path('contact/', views.Contacto, name='contact'),
    
      
]