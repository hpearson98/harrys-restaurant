from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import (
    HomeView, MenuView, AddBookingView, ReservationDetailView, EditBookingView,
    DeleteBookingView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings', views.ReservationList.as_view(), name='bookings'),
    path('menu', MenuView.as_view(), name='menu'),
    path('add-booking', AddBookingView.as_view(), name='add-booking'),
    path(
        'booking-details/<int:pk>',
        ReservationDetailView.as_view(),
        name='booking-details'
    ),
    path(
        'edit-booking/<int:pk>',
        EditBookingView.as_view(),
        name='edit-booking'
    ),
    path(
        'cancel-booking/<int:pk>',
        DeleteBookingView.as_view(),
        name='delete-booking'
    )
]
