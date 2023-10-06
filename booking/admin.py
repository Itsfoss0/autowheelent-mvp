#!/usr/bin/env python3

"""
Register Bookings on the admin dashboard
"""

from django.contrib import admin
from booking.models import Booking


admin.site.register(Booking)
