from . import views
from django.urls import path

urlpatterns = [
    path('bookings.html', views.ReservationList.as_view(), name='bookings'),
]