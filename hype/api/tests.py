from django.test import TestCase
from django.test import Client
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class APITestCase(TestCase):
	def setUp(self):
		pass

	def test_API_checks_for_authentication(self):
		"""Tests whether API checks for authentication
		and return 301 if not authenticated."""
		c = Client()
		response = c.get('/api')
		self.assertEqual(response.status_code, 301)

	def test_API_works_with_authentication(self):
		"""Tests whether API endpoints are visible when
		authenticated."""
		User.objects.create_user('TestUser', None, 'TestPass')
		user = authenticate(username='TestUser', password='TestPass')
		c = Client()
		c.login(username='TestUser', password='TestPass'):
		response = c.get('/api')
		self.assertEqual(response.status_code, 200)
		