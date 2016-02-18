from django.test import TestCase
from django.test import Client
from rest_framework.test import APIClient
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class APITestCase(TestCase):
	def setUp(self):
		user = User.objects.create_user('TestUser', None, 'TestPass')
		user.save()

	def test_API_checks_auth(self):
		"""
		Tests if API root throws 403(Forbidden) if not authenticated
		"""
		client = APIClient()
		response = client.get('/api/')
		self.assertEqual(response.status_code, 403)

	def test_API_works_with_authentication(self):
		"""
		Tests whether API endpoints are visible when authenticated
		"""	
		client = Client()	
		rest_client = APIClient()
		client.login(username='TestUser', password='TestPass')
		rest_client.login(username='TestUser', password='TestPass')
		response = rest_client.get('/api/posts/', format = 'json')
		self.assertEqual(response.status_code, 200)
		