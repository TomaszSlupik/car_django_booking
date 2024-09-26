from django.urls import path
from .views import LoginView, error_login_view

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("error_login/", error_login_view, name="error_login"),
]
