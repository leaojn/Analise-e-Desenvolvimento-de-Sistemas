from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from django.test import TestCase
from users.models import Perfil
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class APITest(TestCase):

    def setUp(self):
        user = User()
        user.username = "teste"
        user.set_password("teste")
        user.save()
        self.token = Token.objects.get(user=user)

    def test_get_token(self, username="teste", password="teste"):
        request_data = {"username": username, "password": password}
        response = self.client.post(reverse('get_auth_token'), data=request_data)
        print(response)
        self.assertEqual(response.status_code, 200)
