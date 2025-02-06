from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.messages import get_messages


class RegisterViewTest(TestCase):
    def setUp(self):
        self.url = reverse('register') 
        self.valid_data = {
            'username': 'janKowalski',
            'email': 'jankowalski@gmail.com',
            'password': 'janekKowal123',
        }

        self.client = APIClient()

    def test_register_get(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'register.html')


    def test_register_success(self):
        res = self.client.post(self.url, self.valid_data)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'register.html')
        
        # Czy został zapisany:
        self.assertTrue(User.objects.filter(username=self.valid_data['username']).exists())
        
        # Komunikat dla użytkownika
        msg = list(get_messages(res.wsgi_request))
        self.assertEqual(str(msg[0]), "Zarejestrowałeś się pomyślnie!")

