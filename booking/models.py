from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


TIME_CHOICES = (
    ('11:00:00', '11am'),
    ('11:30:00', '11:30am'),
    ('12:00:00', '12pm'),
    ('12:30:00', '12:30pm'),
    ('13:00:00', '1pm'),
    ('13:30:00', '1:30pm'),
    ('14:00:00', '2pm'),
    ('14:30:00', '2:30pm'),
    ('15:00:00', '3pm'),
    ('15:30:00', '3:30pm'),
    ('16:00:00', '4pm'),
    ('16:30:00', '4:30pm'),
    ('17:00:00', '5pm'),
    ('17:30:00', '5:30pm'),
    ('18:00:00', '6pm'),
    ('18:30:00', '6:30pm'),
    ('19:00:00', '7pm'),
    ('19:30:00', '7:30pm'),
    ('20:00:00', '8pm'),
    ('20:30:00', '8:30pm'),
    ('21:00:00', '9pm'),
    ('21:30:00', '9:30pm'),
    ('22:00:00', '10pm'),
)


class Reservation(models.Model):
    """
    Defines the fields for the reservation system in the database
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default=""
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default=""
    )
    email = models.EmailField(default="email@hrestaurant.com")
    phone = models.CharField(
        blank=True,
        unique=True,
        default="",
        max_length=15
    )
    number_of_people = models.IntegerField(
        default=2,
        validators=[
            MaxValueValidator(30),
            MinValueValidator(1)
        ]
    )
    date = models.DateField(default=timezone.now())
    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        )
    special_requests = models.CharField(
        max_length=250,
        default=""
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Booking: {self.id} - {self.first_name} {self.last_name}"

    def bookind_date_time(self):
        return f"You're booked in on {self.date} at {self.time}"

    def booking_number(self):
        return f"You're booking number is: {self.id}"
