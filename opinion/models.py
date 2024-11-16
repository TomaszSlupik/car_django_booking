from django.db import models
from booking.models import Booking
from django.contrib.auth.models import User

# Create your models here.
class Opinion(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Opinia od {self.user} oceniona na {self.rating}"