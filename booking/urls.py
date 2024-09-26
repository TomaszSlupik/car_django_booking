from django.urls import path
from .views import booking_view, BookingListView


urlpatterns = [
    path("", booking_view, name="booking"),
    path("list/", BookingListView.as_view(), name="booking_list"),
]
