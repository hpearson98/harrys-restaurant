from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from booking.models import Reservation
from django.utils import timezone


class ReservationForm(ModelForm):
    """
    This is the form class for my booking form.
    It handles all of the fields that the form uses as well as
    any attributes that have been applied to the form field such as
    Bootstrap classes
    """
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

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'number_of_people': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'time': forms.Select(attrs={
                'class': 'form-control'
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

    def clean_date(self):
        booking_date = self.cleaned_data['date']
        if booking_date < timezone.now().date():
            raise ValidationError("Date selected is before current date!")
            
        return booking_date
