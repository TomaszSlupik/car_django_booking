"""
URL configuration for car_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from users.views import (
    LoginView,
    RegisterView,
    error_login_view,
    come_back_to_main_page, 
)


from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from booking.views import BookingDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(), name="login"),
    path("error_login", error_login_view, name="error_login"),
    path("", come_back_to_main_page, name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("main/", include("main.urls")),
    path("main/booking/", include("booking.urls")),
    path("main/opinion/", include("opinion.urls")),
    path("main/contact/", include("contact.urls")),
    path("main/aboutus/", include("aboutus.urls")),
    path('main/delete/<int:booking_id>/', BookingDeleteView.as_view(), name='booking_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)