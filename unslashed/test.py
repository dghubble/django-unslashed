from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.test import TestCase, Client

from django.middleware.common import CommonMiddleware
from unslashed.middleware import RemoveSlashMiddleware

class RemoveSlashMiddlewareTest(TestCase):
  def setUp(self):
    self.client = Client()

  def test_permanent_redirect_to_non_slashed(self):
    response = self.client.get('/testapps/', follow=False)
    self.assertIsInstance(response, HttpResponsePermanentRedirect)
    self.assertFalse(response['Location'].endswith('/'))

    response = self.client.get('/testapps/1/', follow=False)
    self.assertIsInstance(response, HttpResponsePermanentRedirect)
    self.assertFalse(response['Location'].endswith('/'))

  def test_no_redirect_when_slash_url_is_valid(self):
    response = self.client.get('/testapps/1/urlendsinslash/', follow=False)
    self.assertIsInstance(response, HttpResponse)
    self.assertEqual(response.status_code, 200)
    
  def test_no_redirect_when_slashed_and_unslashed_invalid(self):
    response = self.client.get('/testapps/invalid/', follow=False)
    self.assertNotIsInstance(response, HttpResponsePermanentRedirect)

    response = self.client.get('/testapps/invalid', follow=False)
    self.assertNotIsInstance(response, HttpResponsePermanentRedirect)

  def tearDown(self):
    del self.client