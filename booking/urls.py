from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('bookings.html', views.ReservationList.as_view(), name='bookings'),
    path("", TemplateView.as_view(template_name="index.html")),
]
