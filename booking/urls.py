from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, MenuView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bookings.html', views.ReservationList.as_view(), name='bookings'),
    path('menu.html', MenuView.as_view(), name='menu'),
]
