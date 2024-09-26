from django.shortcuts import render
from django.views.generic import ListView
from .models import Booking

# Create your views here.
def booking_view (request):
    return render(request, "booking.html")

class BookingListView(ListView):
    model = Booking
    template_name = 'booking.html'
    context_object_name = 'bookings' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookings'] = Booking.objects.all()  
        return context

