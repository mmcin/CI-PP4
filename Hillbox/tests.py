from django.test import TestCase
from .forms import SiteUpload, GalleryUpload, ContactForm

# class TestDjango(TestCase):

#     def test_this_thing_works(self):
#         self.assertEqual(1,0)

# form validation 
class TestFormValidation(TestCase):
    def test_site_upload_form(self):
        form = SiteUpload({'site_name': "", 'pilot': "jim", 'wind_direction': "N", 'overview':'cornflakes', 'landing_information':'some text', 'warnings':'some text', 'featured_image':"", 'status':1})
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(form.errors['site_name'][0], 'This field is required.')

    def test_gallery_upload_form(self):
        form = GalleryUpload({'featured_image':"", 'site_name':"", 'status':1,})
        self.assertFalse(form.is_valid())
        self.assertIn('site_name', form.errors.keys())
        self.assertEqual(form.errors['site_name'][0], 'This field is required.')

    def test_contact_form(self):
        form = ContactForm({'first_name':"", 'email_address':"", 'message':"",})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

# views
class TestViews(TestCase):
    def test_get_flying_sites(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_add_site(self):

    # def test_edit_site(self):

    # def test_delete_site(self):
