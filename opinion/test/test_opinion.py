import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from booking.models import Booking
from opinion.models import Opinion


class AddOpinionTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_usera", password="test12345")
        self.url = reverse('add_opinion')

        self.booking = Booking.objects.create(id=1, user=self.user)

        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)
        self.client = APIClient()

    def test_add_opinion(self):

        data_opinion = {
            "booking": self.booking.id,
            "rating": 5,
            "comment": "Świetna usługa!"
        }
        # Przesyłam dane jako JSON
        res = self.client.post(
            self.url,
            data=json.dumps(data_opinion),  
            content_type='application/json', 
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )

        self.assertEqual(res.status_code, 200)

        

        response_data = json.loads(res.content)
        print(response_data)
        
        self.assertEqual(response_data['success'], True)
        self.assertEqual(response_data['message'], 'Opinia została dodana pomyślnie!')
        self.assertEqual(Opinion.objects.count(), 1) 
