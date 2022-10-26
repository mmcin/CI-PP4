from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('not_authorised', views.NotAuthorised, name='not_authorised'),
    path('sites/', views.SiteList.as_view(), name='sites'),
    path('gallery/', views.PhotoList.as_view(), name='gallery'),
    path('edit/<site_id>', views.EditSite, name='edit'),
    path('delete/<site_id>', views.DeleteSite, name='delete'),
    path('sites/<slug:slug>/', views.SiteDetail.as_view(), name='site_detail'),
    path('site_comment_edit/<comment_id>', views.EditComment, name='site_comment_edit'),
]