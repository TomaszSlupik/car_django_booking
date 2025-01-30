from django.test import TestCase
from booking.models import Booking
from django.urls import reverse


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


