from django.urls import path
from .views import opinion_view, add_opinion

urlpatterns = [
    path("", opinion_view, name="opinions"),
     path("add/", add_opinion, name="add_opinion"),
    
]