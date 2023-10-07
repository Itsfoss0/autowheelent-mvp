#!/usr/bin/env python3

"""
Urls for bookings
"""

from django.urls import path

from booking.views import booking

urlpatterns = [
    path('', booking, name='booking')
]