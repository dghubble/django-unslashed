from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.test import TestCase, Client
from django.utils.http import urlquote


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

    def test_permanent_redirect_to_unslashed_when_url_has_plus_signs(self):
        response = self.client.get('/testapps/url+with+plus/', follow=False)
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertFalse(response['Location'].endswith('/'))
        self.assertRegexpMatches(response['Location'], r'/url\+with\+plus$')

        response = self.client.get('/testapps/url+with+plus/?param1=1&param2=%2Bfoo', follow=False)
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertRegexpMatches(response['Location'], r'/url\+with\+plus\?param1=1&param2=%2Bfoo$')

    def test_permanent_redirect_to_unslashed_when_url_has_urlencoded_chars(self):
        # urlquote is used because django.test.Client decodes the URL
        # which goes against the test
        slashed_url = urlquote('/testapps/quoted/foo%2Bbar%23baz%20/')
        response = self.client.get(slashed_url, follow=False)
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertFalse(response['Location'].endswith('/'))
        self.assertRegexpMatches(response['Location'], r'/quoted/foo%2Bbar%23baz%20$')

        response = self.client.get(slashed_url + '?param1=1&param2=%2Btest', follow=False)
        self.assertIsInstance(response, HttpResponsePermanentRedirect)
        self.assertRegexpMatches(response['Location'], r'/quoted/foo%2Bbar%23baz%20\?param1=1&param2=%2Btest$')

    def test_no_redirect_when_slash_url_is_valid(self):
        response = self.client.get('/testapps/1/urlendsinslash/', follow=False)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)

    def test_no_redirect_when_slashed_and_unslashed_invalid(self):
        response = self.client.get('/testapps/invalid/', follow=False)
        self.assertNotIsInstance(response, HttpResponsePermanentRedirect)
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/testapps/invalid', follow=False)
        self.assertNotIsInstance(response, HttpResponsePermanentRedirect)
        self.assertEqual(response.status_code, 404)

    def test_warns_about_redirect_and_post(self):
        with self.settings(DEBUG=True):
            with self.assertRaises(RuntimeError):
                self.client.post('/testapps/', follow=False)

    def tearDown(self):
        del self.client
