from django.urls import path
from .views import BookingListView, BookingView, BookingSearchView, BookingUserListView, BookingDeleteView


urlpatterns = [
    path('user/', BookingUserListView.as_view(), name='booking_user_view'),
    path("", BookingListView.as_view(), name="booking_list"),
    path("main/booking/", BookingView.as_view(), name='booking'),
    path("", BookingSearchView.as_view(), name="booking_search"),
    
]
