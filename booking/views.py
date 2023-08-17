from django.shortcuts import render

from django.views.generic import TemplateView, FormView, ListView, DetailView

from django.http import HttpResponseRedirect

from .models import Reservation

from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
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


class AddBookingView(FormView):
    template_name = "add_booking.html"
    form_class = ReservationForm
    success_url = "bookings"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
