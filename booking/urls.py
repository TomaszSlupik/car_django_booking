from django.urls import path
from .views import BookingListView, BookingView, BookingSearchView, booking_user_view


urlpatterns = [
    path("user", booking_user_view, name="user"),
    path("", BookingListView.as_view(), name="booking_list"),
    path("main/booking/", BookingView.as_view(), name='booking'),
    path("", BookingSearchView.as_view(), name="booking_search"),
]
