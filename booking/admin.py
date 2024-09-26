from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name_car_booking", "image_car", "is_booked")
