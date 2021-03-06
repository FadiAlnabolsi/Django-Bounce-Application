from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth.views import login, logout
from links.views import home
from links.models import Link
# Create your tests here.

class HomeTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        view_found = resolve('/')
        self.assertEqual(view_found.func, home)

    def test_home_template_used_by_home_view(self):
    	response = self.client.get(reverse('home'))
    	self.assertTemplateUsed(response, 'home.html')

    def test_most_recent_links_returned_by_home_view(self):
    	response = self.client.get(reverse('home'))
    	response_links = response.context['links']
    	expected_links = Link.objects.all().order_by('-submitted')[:15]
    	self.assertQuerysetEqual(response_links, expected_links)

class AuthTest(TestCase):

    def test_login_url_resolves_to_login_view(self):
        view_found = resolve('/login/')
        self.assertEqual(view_found.func, login)

    def test_login_template_used_by_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout_url_resolves_to_logout_view(self):
        view_found = resolve('/logout/')
        self.assertEqual(view_found.func, logout)
