from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('bookings.html', views.ReservationList.as_view(), name='bookings'),
]
