from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email", "number_of_people"]


admin.site.register(Reservation, ReservationAdmin)
