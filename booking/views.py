from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Reservation

from .forms import ReservationForm
from allauth.account.views import LoginView


class ReservationList(LoginRequiredMixin, ListView):
    """
    This is the view that displays the list of reservations
    on the Bookings page.
    It orders the bookings by date and and displays the bookings
    created by the currently authenticated user.
    """
    model = Reservation
    queryset = Reservation.objects.order_by('date')
    template_name = 'bookings.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    def get_queryset(self):
        return Reservation.objects.filter(booking_creator=self.request.user)


class ReservationDetailView(LoginRequiredMixin, DetailView):
    """
    This is the view for the booking_details.html template.
    It simply renders the booking details of the selected booking.
    """
    model = Reservation
    template_name = 'booking_details.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'


class HomeView(TemplateView):
    """
    This is the view for the Home Page
    """
    template_name = "index.html"


class MenuView(TemplateView):
    """
    This is the view for the Menu Page
    """
    template_name = "menu.html"


class AddBookingView(LoginRequiredMixin, CreateView):
    """
    This is the View for the Add Booking Form
    """
    model = Reservation
    form_class = ReservationForm
    template_name = "add_booking.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'

    def form_valid(self, form):
        form.instance.booking_creator = self.request.user
        return super().form_valid(form)


class EditBookingView(LoginRequiredMixin, UpdateView):
    """
    This is the view for the Edit booking form
    """
    model = Reservation
    form_class = ReservationForm
    template_name = "edit_booking.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'


class DeleteBookingView(LoginRequiredMixin, DeleteView):
    """
    This is the view for the delete_booking.html template
    """
    model = Reservation
    template_name = "delete_booking.html"
    success_url = reverse_lazy('bookings')
    login_url = '/accounts/login/'
    redirect_field_name = 'account_login'
