from datetime import date
from django.test import Client, TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from cinemaapp.forms import MovieForm
from cinemaapp.models import Actor, Movie

# Create your tests here.
class MovieViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_admin = User.objects.create_user(username='admin', password='admin')
        self.user_other = User.objects.create_user(username='other', password='other')
        self.admin_role = Group.objects.create(name='Admin')
        content_type = ContentType.objects.get_for_model(Movie)
        add_permission = Permission.objects.get(codename='add_movie', content_type=content_type)
        change_permission = Permission.objects.get(codename='change_movie', content_type=content_type)
        delete_permission = Permission.objects.get(codename='delete_movie', content_type=content_type)
        view_permission = Permission.objects.get(codename='view_movie', content_type=content_type)
        self.admin_role.permissions.add(add_permission)
        self.admin_role.permissions.add(change_permission)
        self.admin_role.permissions.add(delete_permission)
        self.admin_role.permissions.add(view_permission)
        self.user_admin.groups.add(self.admin_role)
    
    def test_form(self):
        self.client.login(username='admin', password='admin')
        url = reverse('form')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_form_no_permission(self):
        self.client.login(username='other', password='other')
        url = reverse('form')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
    
    def test_form_not_logged_in(self):
        url = reverse('form')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)