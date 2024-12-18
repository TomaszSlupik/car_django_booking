from django.contrib import admin
from .models import Booking
from django.utils import formats

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name_car_booking", "image_car", "is_booked", "formated_start_date", "formated_end_date", "user")


    def formated_start_date(self, object):
        return formats.date_format(object.start_date, "SHORT_DATE_FORMAT") if object.start_date else "Brak daty rezerwacji"
    
    def formated_end_date(self, object):
        return formats.date_format(object.end_date, "SHORT_DATE_FORMAT") if object.end_date else "Brak daty rezerwacji"