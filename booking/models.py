from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_first_name")
    last_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_last_name")
    email = models.EmailField()


class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reserved_table")
    party = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="booking_name")
    slot = models.DateField()
