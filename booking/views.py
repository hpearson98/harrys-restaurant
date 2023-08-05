from django.shortcuts import render
from django.views import generic
from .models import Reservation
from django.views.generic import TemplateView


# From 'View Creation Checklist' Code Institute video
class ReservationList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.order_by('date')
    template_name = 'bookings.html'


class HomeView(TemplateView):
    template_name = "index.html"
