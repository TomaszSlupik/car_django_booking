import json
from django.test import TestCase
from booking.models import Booking
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')

    def test_booking(self):
        booking = Booking.objects.create(
            name_car_booking='Testowy samochód',
            image_car=None,  
            is_booked=False,
            start_date='2025-02-06',
            end_date='2025-02-28',
            user=self.user
        )
        
        self.assertEqual(booking.name_car_booking, 'Testowy samochód')
        self.assertEqual(booking.is_booked, False)
        self.assertEqual(booking.start_date, '2025-02-06')
        self.assertEqual(booking.end_date, '2025-02-28')
        self.assertEqual(booking.user, self.user)

    def test_str_book(self):
        booking = Booking(name_car_booking='Testowa Honda')
        self.assertEqual(str(booking), 'Testowa Honda')



class BookingListViewTest (TestCase):
    
    # Tworzę symulację danych:
    def setUp(self):
        self.booking_1 = Booking.objects.create(name_car_booking='Hyundai i30', is_booked=True)
        self.booking_2 = Booking.objects.create(name_car_booking='Toyota Corolla', is_booked=False)
        self.booking_3 = Booking.objects.create(name_car_booking='Ford Focus', is_booked=True)
        self.booking_4 = Booking.objects.create(name_car_booking='Volvo xc90', is_booked=False)

        self.url = reverse('booking_list')

    # sprawdzam czy są zarezerwowane:
    def test_is_booked_true(self):

        res = self.client.get(self.url, {'is_booked': 'true'})
        self.assertEqual(res.status_code, 200)
        
        bookings = res.context['bookings']

        self.assertEqual(len(bookings), 2)
        self.assertIn(self.booking_1, bookings)
        self.assertIn(self.booking_3, bookings)

    # czy nie są zarezerwowane:
    def test_is_booked_false(self):

        res = self.client.get(self.url, {'is_booked': 'false'})
        self.assertEqual(res.status_code, 200)
        
        bookings = res.context['bookings']

        self.assertEqual(len(bookings), 2)
        self.assertIn(self.booking_2, bookings)
        self.assertIn(self.booking_4, bookings)

    # czy mam wszystkie rekordy:
    def test_all_data(self):
        
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        
        bookings = res.context['bookings']

        self.assertEqual(len(bookings), 4)
        self.assertIn(self.booking_1, bookings)
        self.assertIn(self.booking_2, bookings)
        self.assertIn(self.booking_3, bookings)
        self.assertIn(self.booking_4, bookings)


class BookingSearchViewTest (TestCase):

    def setUp(self):
        self.car_1 = Booking.objects.create(name_car_booking='Kia Proceed')
        self.car_2 = Booking.objects.create(name_car_booking='Kia Sportage')
        self.car_3 = Booking.objects.create(name_car_booking='Opel Astra')
        self.car_4 = Booking.objects.create(name_car_booking='Kia Insignia')

        self.url = reverse('booking_search')

    # czy wyszukam podane samochody:
    def test_search_car(self):
        
        res = self.client.get(self.url, {'car_name': 'Kia'})
        self.assertEqual(res.status_code, 200)

        bookings = res.context['bookings']
        self.assertEqual(len(bookings), 3)
        self.assertTrue(all('Kia' in booking.name_car_booking for booking in bookings))

        self.assertIn(self.car_1, bookings)
        self.assertIn(self.car_2, bookings)
        self.assertIn(self.car_4, bookings)
        self.assertNotIn(self.car_3, bookings)  

    # Czy zwróci zero rekordów:
    def test_search_car_no_results(self):

        res = self.client.get(self.url, {'car_name': 'BMW'})
        self.assertEqual(res.status_code, 200)

        bookings = res.context['bookings']
        self.assertEqual(len(bookings), 0)


class BookingViewTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testowy_uzytkownik', password='test123')
        self.booking = Booking.objects.create(name_car_booking='Peugeot')

        self.url = reverse('booking') 

    def test_booking_success(self):

        today = datetime.today().date() 
        data = {
            'booking_id': self.booking.id,
            'start_date': today.strftime('%Y-%m-%d'),
            'end_date': '2025-02-28',
            'username': self.user.username
        }

        # POST z danymi
        res = self.client.post(self.url, json.dumps(data), content_type='application/json')


        self.assertEqual(res.status_code, 200)
        
        res_data = json.loads(res.content)
        self.assertEqual(res_data['status'], 'success')

        # czy rezerwacja została poprawnie zarezerwowana 
        self.booking.refresh_from_db()  
        self.assertTrue(self.booking.is_booked)
        self.assertEqual(self.booking.start_date, today) 
        self.assertEqual(self.booking.end_date, datetime.strptime('2025-02-28', '%Y-%m-%d').date())
        self.assertEqual(self.booking.user, self.user)  


    # dodanie sprawdzeia na poprawność rezerwacji dat:
    def test_end_date_before_start_date(self):
        data = {
            'booking_id': self.booking.id,
            'start_date': '2025-02-28',
            'end_date': '2025-02-06',
            'username': 'test'
        }

        response = self.client.post(reverse('booking'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'error', 'message': 'Data końcowa nie może być wcześniejsza niż data początkowa.'})


    # dodanie sprawdzenia na początkową datę do dzisiejszej 
    def test_start_date_before_today(self):
        data = {
            'booking_id': self.booking.id,
            'start_date': '2025-02-07',
            'end_date': '2025-02-28',
            'username': 'test'
        }

        response = self.client.post(reverse('booking'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'error', 'message': 'Data rozpoczęcia nie może być wcześniejsza niż dzisiejsza.'})