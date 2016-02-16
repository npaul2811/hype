from django.test import TestCase
from django.test import Client

class BlogTestCase(TestCase):
	def setUp(self):
		pass

	def test_index_is_mapped_correctly(self):
		"""Tests whether index is mapped properly"""
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code, 200)