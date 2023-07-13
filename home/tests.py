from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from home.models import ShortURL

class ShortenURLTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_short_url_api')
        self.valid_payload = {
            'original_url': 'https://www.example.com'
        }
        self.invalid_payload = {
            'original_url': 'invalid_url'
        }

    def test_shorten_url_valid_payload(self):
        response = self.client.post(self.url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('original_url', response.data)
        self.assertIn('short_url', response.data)

class RedirectURLViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.short_url_obj = ShortURL.objects.create(
            original_url='https://www.example.com',
            short_url='abcd'
        )
        self.url = reverse('get_original_url', kwargs={'short_code': 'abcd'})

    def test_redirect_url(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, self.short_url_obj.original_url)



