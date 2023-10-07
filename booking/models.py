#!/usr/bin/env python3

"""
Bookings Model
"""

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta

from cars.models import Car

class BookingDate(models.DateTimeField):
    """
    Overriding the DateTimeFiled's default date
    """
    def get_default(self):
        """
        The default datetime to 1 day from now
        """
        return datetime.now() + timedelta(days=1)

class Booking(models.Model):
    """
    Bookings
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    booking_date = BookingDate(verbose_name='Booking Date')


    def __str__(self):
        return f'{self.user.first_name}: {self.pickup_location}'



