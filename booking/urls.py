from django.urls import path
from .views import BookingListView, BookingView, BookingSearchView


urlpatterns = [
    # path("", booking_view, name="booking"),
    path("", BookingListView.as_view(), name="booking_list"),
    path("main/booking/", BookingView.as_view(), name='booking'),
    path("", BookingSearchView.as_view(), name="booking_search"),
]
