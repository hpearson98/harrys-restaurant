from django.forms import ModelForm
from booking.models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'number_of_people',
            'date',
            'time',
            'special_requests',
        ]
