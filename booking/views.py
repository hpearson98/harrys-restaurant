from django.shortcuts import render

from django.views import generic
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect

from .models import Reservation

from .forms import ReservationForm


# From 'View Creation Checklist' Code Institute video
class ReservationList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.order_by('date')
    template_name = 'bookings.html'


class HomeView(TemplateView):
    template_name = "index.html"


class MenuView(TemplateView):
    template_name = "menu.html"


def get_name(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        """
        if form.is_valid():
            return HttpResponseRedirect('/confirmation/')
        """
    # if a GET method (or any other method), it will create a blank form
    else:
        form = ReservationForm()

    return render(request, 'add_booking.html', {'form': form})
