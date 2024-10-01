from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    name_car_booking = models.CharField(max_length=50)
    image_car = models.ImageField(upload_to="photos/", null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.name_car_booking
    


