from django.test import TestCase
from django.urls import reverse
from django.urls import resolve

from .views import signup

class SignUpTest(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def tst_signup_url_resolvers_signup_view(self):
        view = resolve('/signup')
        self.assertEquals(view.func, signup)
