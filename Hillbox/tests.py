from django.test import TestCase
from .forms import SiteUpload, GalleryUpload

# class TestDjango(TestCase):

#     def test_this_thing_works(self):
#         self.assertEqual(1,0)

class TestSiteUploadForm(TestCase):
    def test_site_upload_form(self):
        form = SiteUpload({'site_name': "", 'pilot': "jim", 'wind_direction': "N", 'overview':'gjhg', 'landing_information':'some text', 'warnings':'some text', 'featured_image':"", 'status':1})
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(form.errors['site_name'][0], 'This field is required.')

class TestGalleryForm(TestCase):
    def test_gallery_upload_form(self):
        form = GalleryUpload({'featured_image':"", 'site_name':"", 'status':1,})
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(form.errors['site_name'][0], 'This field is required.')