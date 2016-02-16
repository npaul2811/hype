from django.test import TestCase
from django.test import Client

class APITestCase(TestCase):
	def setUp(self):
		pass

	def test_API_checks_for_authentication(self):
		"""Tests whether API checks for authentication
		and return 301 if not authenticated."""
		c = Client()
		response = c.get('/api')
		self.assertEqual(response.status_code, 301)