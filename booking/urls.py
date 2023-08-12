from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, MenuView, AddBookingView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings.html', views.ReservationList.as_view(), name='bookings'),
    path('menu.html', MenuView.as_view(), name='menu'),
    path('add_booking.html', AddBookingView.as_view(), name='add-booking'),
]
