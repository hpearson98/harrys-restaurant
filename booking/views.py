from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView, DetailView

from django.http import HttpResponseRedirect

from .models import Reservation

from .forms import ReservationForm
from allauth.account.views import LoginView


class ReservationList(ListView):
    model = Reservation
    queryset = Reservation.objects.order_by('date')
    template_name = 'bookings.html'


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'booking_details.html'


class HomeView(TemplateView):
    template_name = "index.html"


class MenuView(TemplateView):
    template_name = "menu.html"


class AddBookingView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "add_booking.html"

