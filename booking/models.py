from django.db import models

# Create your models here.
class Booking(models.Model):
    name_car_booking = models.CharField(max_length=50)
    image_car = models.ImageField(upload_to="photos/", null=True, blank=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name_car_booking
    


