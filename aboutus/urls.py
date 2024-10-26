from django.urls import path
from .views import aboutus_view

urlpatterns = [
    path("", aboutus_view, name="aboutus"),
]