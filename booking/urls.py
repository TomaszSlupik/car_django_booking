from django.urls import path
from .views import BookingListView, BookingView


urlpatterns = [
    # path("", booking_view, name="booking"),
    path("", BookingListView.as_view(), name="booking_list"),
    path("main/booking/", BookingView.as_view(), name='booking')
]
