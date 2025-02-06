from django.test import TestCase
from django.urls import reverse

class AboutUsViewTest(TestCase):
    def test_aboutus_view(self):
        response = self.client.get(reverse('aboutus'))  
        self.assertEqual(response.status_code, 200)

    def test_aboutus_template_used(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'aboutus.html')
