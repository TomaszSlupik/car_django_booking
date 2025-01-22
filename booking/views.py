from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Booking
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from django.http import JsonResponse
from datetime import datetime
import json

# Create your views here.
def booking_view (request):
    return render(request, "booking.html")

class BookingListView(ListView):
    # permission_classes = [IsAuthenticated] 
    model = Booking
    template_name = 'booking.html'
    context_object_name = 'bookings' 

    def get_queryset(self):
        queryset  = Booking.objects.all()

        car_name = self.request.GET.get('car_name', "")
        is_booked = self.request.GET.get('is_booked', None)

        if car_name:
            queryset  = queryset.filter(name_car_booking=car_name)
        if is_booked is not None:
            is_booked = is_booked.lower() == 'true' 
            queryset = queryset.filter(is_booked=is_booked)

        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookingView(View):
    def post(self, request, **kwargs):
        try:
            data = json.loads(request.body)
            booking_id = data.get('booking_id')
            start_date = data.get('start_date')
            end_date = data.get('end_date')  
            username = data.get('username')  

            print("Otrzymano zapytanie z booking_id:", booking_id)

            if booking_id:
                try:
                    booking = Booking.objects.get(id=booking_id)

                    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
                    booking.is_booked = True
                    booking.start_date = start_date_obj
                    booking.end_date = end_date_obj
                    if username:  
                        try:
                            user = User.objects.get(username=username)  
                            booking.user = user  
                        except User.DoesNotExist:
                            print(f"Nie znaleziono użytkownika o nazwie: {username}")
                            booking.user = None  
                    else:
                        # Jeśli użytkownik jest zalogowany, przypisuję go do booking.user
                        if request.user.is_authenticated:
                            booking.user = request.user

                    booking.save()
                    print("Rezerwacja zaktualizowana:", booking_id)
                    return JsonResponse({'status': 'success', 'message': 'Zarezerwowano'})
                except Booking.DoesNotExist:
                    print("Nie znaleziono rezerwacji z ID:", booking_id)  
                    return JsonResponse({'status': 'error', 'message': 'Nie znaleziono rezerwacji'})
            else:
                print("Nieprawidłowe ID rezerwacji:", booking_id)  
                return JsonResponse({'status': 'error', 'message': 'Nieprawidłowe ID rezerwacji'})
        
        except json.JSONDecodeError:
            print("Błędny format danych:", request.body) 
            return JsonResponse({'status': 'error', 'message': 'Błędny format danych'})